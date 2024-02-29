import re

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from django.forms.models import model_to_dict
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.utils import extend_schema, OpenApiParameter

from . import serializers
from .models import RefLokasiTree, RefLokasiTreeUpdate

from base.custom_pagination import CustomPagination
from base.response import response__, get_response, post_update_response, not_found, response_basic


class TreeJaringanViews(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    queryset = RefLokasiTree.objects.all()
    serializer_class = serializers.RefLokasiSerializer
    serializer_update_class = serializers.BatchRefLokasiSerializer

    pagination_class = CustomPagination

    def get_tree(self, ref_lokasi_tree):
        # tree = model_to_dict(ref_lokasi_tree, fields=['id_ref_lokasi', 'nama_lokasi',
        #                                               'id_parent_lokasi'])
        tree = model_to_dict(ref_lokasi_tree)
        tree['nama_jenis_lokasi'] = ref_lokasi_tree.nama_jenis_lokasi 
        if ref_lokasi_tree.children_gardu_induk.all().exists():
            children = list()
            # print(ref_lokasi_tree.nama_jenis_lokasi)  
            for child in ref_lokasi_tree.children_gardu_induk.all(): 
                id_ref_jenis_lokasi = child.id_ref_jenis_lokasi.id_ref_jenis_lokasi  
                if id_ref_jenis_lokasi != 5: 
                    children.append(self.get_tree(child))
            tree['children'] = children
        return tree
        print(ref_lokasi_tree.id_ref_jenis_lokasi)
        if ref_lokasi_tree.id_ref_jenis_lokasi == 4:
            if ref_lokasi_tree.children_gardu_induk.all().exists():
                children = list()
                for child in ref_lokasi_tree.children.all():
                    children.append(self.get_tree(child))
                tree['children'] = children
        else:
            if ref_lokasi_tree.children.all().exists():
                children = list()
                for child in ref_lokasi_tree.children.all():
                    children.append(self.get_tree(child))
                tree['children'] = children
        return tree

    @extend_schema(
        methods=["GET"],
        summary="Get Master Data - Tree Jaringan.",
        description="Get Master Data - Tree Jaringan.",
        parameters=[
            OpenApiParameter(name='page', description='page number. isi -1 jika mau tanpa pagination.', required=False,
                             type=str, default=1),
            OpenApiParameter(name='limit', description='limit data per page', required=False, type=str, default=10),
            OpenApiParameter(name='id_ref_lokasi', description='multiple, split by comma.',
                             required=False, type=str),
        ],
        request=serializer_class,
        responses=serializer_class,
        tags=['master_jaringan']
    )
    def list(self, request):
        id_ref_lokasi = request.GET.get('id_ref_lokasi')
        if not id_ref_lokasi:
            # q_set = self.get_queryset().filter(id_parent_lokasi__isnull=True)\
            #     .filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')
            q_set = self.get_queryset().filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')

            queryset = self.filter_queryset(
                q_set
            )

            return get_response(self, request, queryset, 'tree_jaringan.view')
        else:
            id_ref_lokasi = id_ref_lokasi.strip()
            id_ref_lokasi = id_ref_lokasi.split(',')
            # q_set = self.get_queryset().filter(id_parent_lokasi__isnull=True).filter(id_ref_lokasi__in=id_ref_lokasi)\
            #     .filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')
            q_set = self.get_queryset().filter(id_ref_lokasi__in=id_ref_lokasi)\
                .filter(tree_jaringan=1).order_by('id_parent_lokasi', 'nama_lokasi')

            final_tree = list()
            for ref_lokasi_tree in q_set:
                final_tree.append(self.get_tree(ref_lokasi_tree))

            return response_basic(_status=True, results=final_tree, msg='tree_jaringan.view')

    # update batch
    def get_data(self, obj_id):
        try:
            data_tree = RefLokasiTreeUpdate.objects.get(id_ref_lokasi=obj_id)
            return True, data_tree
        except Exception as e:
            return False, e

    @extend_schema(
        methods=["PUT"],
        summary="Get Master Data - Tree Jaringan - Update Data Parent Jaringan.",
        description="Get Master Data - Tree Jaringan - Update Data Parent Jaringan, Can Be Multiple Update.",
        request=serializer_update_class,
        responses=serializer_update_class,
        tags=['master_jaringan']
    )
    @action(detail=False, methods=['PUT'],
            url_path='update-data-parent', url_name='update_data_parent')
    def batch(self, request):
        update_data = request.data
        is_many = isinstance(update_data, list)
        if is_many:
            instances = []
            for data in update_data:
                id_ref_lokasi = data['id_ref_lokasi']
                id_parent_lokasi = data['id_parent_lokasi']

                _, obj = self.get_data(id_ref_lokasi) 
                if _:
                    if obj.id_ref_jenis_lokasi == 6: 
                        obj.id_gardu_induk = id_parent_lokasi
                    else:
                        obj.id_parent_lokasi = id_parent_lokasi
                        
                    obj.save()
                    instances.append(self.serializer_update_class(instance=obj).data)

            if instances:
                return response_basic(_status=True, results=instances, msg='tree_jaringan.update')
            else:
                return response_basic(msg='tree_jaringan.update_failed')
        else:
            id_ref_lokasi = update_data['id_ref_lokasi']
            id_parent_lokasi = update_data['id_parent_lokasi']

            _, obj = self.get_data(id_ref_lokasi) 
            if _:
                if obj.id_ref_jenis_lokasi == 6: 
                    obj.id_gardu_induk = id_parent_lokasi
                else:
                    obj.id_parent_lokasi = id_parent_lokasi 
                obj.save()

                return response_basic(_status=True,
                                      results=self.serializer_update_class(instance=obj).data,
                                      msg='tree_jaringan.update')
            else:
                return response_basic(msg='tree_jaringan.update_failed')
