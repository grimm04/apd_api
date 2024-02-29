"""
URL definitions for the api.
"""
from apps.patches import routers

from apps.tests.send_email.urls import router as send_mail
from apps.tests.multi_insert.trans_rekap_padam.urls import router as test_rekap_padam

from apps.master.jaringan.ref_jenis_lokasi.urls import router as ref_jenis_lokasi 
from apps.master.jaringan.ref_jenis_pembangkit.urls import router as ref_jenis_pembangkit 
from apps.master.jaringan.ref_lokasi.urls import router as ref_lokasi 
from apps.master.jaringan.ref_lokasi_gd.urls import router as ref_lokasi_gd
from apps.master.jaringan.ref_pemilik_jaringan.urls import router as ref_pemilik_jaringan
from apps.master.jaringan.tree_jaringan.urls import router as tree_jaringan

#master wilayah
from apps.master.wilayah.ref_province.urls import router as ref_province
from apps.master.wilayah.ref_regency.urls import router as ref_regency
from apps.master.wilayah.ref_district.urls import router as ref_district

#master aset
from apps.master.aset.ref_aset.urls import router as ref_aset
from apps.master.aset.ref_aset_doc.urls import router as ref_aset_doc
from apps.master.aset.ref_aset_ex_atr.urls import router as ref_aset_ex_atr
from apps.master.aset.ref_aset_ext_atr.urls import router as ref_aset_ext_atr
from apps.master.aset.ref_aset_jenis.urls import router as ref_aset_jenis
from apps.master.aset.ref_aset_manufaktur.urls import router as ref_asetm_manufaktur
from apps.master.aset.ref_aset_lantai.urls import router as ref_aset_lantai
from apps.master.aset.ref_aset_ruangan.urls import router as ref_aset_ruangan
from apps.master.aset.ref_aset_rak.urls import router as ref_aset_rak
from apps.master.aset.ref_aset_kondisi.urls import router as ref_aset_kondisi
from apps.master.aset.ref_aset_level.urls import router as ref_aset_level
from apps.master.aset.ref_aset_status.urls import router as ref_aset_status
from apps.master.aset.ref_aset_jenis_mutasi.urls import router as ref_aset_jenis_mutasi

#management_upload
from apps.master.management_upload.urls import router as management_upload
from apps.master.management_upload.unit_pembangkit.urls import router as unit_pembangkit
from apps.master.management_upload.pembangkit.urls import router as pembangkit
from apps.master.management_upload.gardu_induk.urls import router as gardu_induk
from apps.master.management_upload.trafo_gi.urls import router as trafo_gi
from apps.master.management_upload.penyulang.urls import router as penyulang
from apps.master.management_upload.zona.urls import router as zona
from apps.master.management_upload.section.urls import router as section
from apps.master.management_upload.segment.urls import router as segment
from apps.master.management_upload.gardu_distribusi.urls import router as gardu_distribusi
from apps.master.management_upload.trafo_gd.urls import router as trafo_gd
from apps.master.management_upload.gardu_hubung.urls import router as gardu_hubung
from apps.master.management_upload.kantor.urls import router as kantor


 

#master wr
from apps.master.wr.ref_wr_status.urls import router as ref_wr_status

#master pegawai
from apps.master.pegawai.departemen.urls import router as pegawai_departemen
from apps.master.pegawai.jabatan.urls import router as pegawai_jabatan
from apps.master.pegawai.perusahaan.urls import router as pegawai_perusahaan
from apps.master.pegawai.ref_pegawai.urls import router as ref_pegawai
from apps.master.pegawai.ref_regu_petugas.urls import router as ref_regu_petugas

#application setting
from apps.application_setting.urls import router as application_setting

#working_management
from apps.master.working_permit.pertanyaan_qrc.urls import router as pertanyaan_qrc
from apps.master.working_permit.risk_point_qrc.urls import router as risk_point_qrc
from apps.master.working_permit.larangan_tanggung_jawab_mitra.urls import router as larangan_tanggung_jawab_mitra
from apps.master.working_permit.approval_management_wp.urls import router as approval_management_wp
from apps.master.working_permit.wm_bagian.urls import router as wp_bagian
from apps.master.working_permit.ref_kel_keselamatan.urls import router as ref_kel_keselamatan
from apps.master.working_permit.ref_kel_pekerjaan.urls import router as ref_kel_pekerjaan

#trans
from apps.trans.trans_pm_jenis_doc.urls import router as trans_pm_jenis_doc
from apps.trans.opsisdis.trans_wo_log_status.urls import router as trans_wo_log_status
from apps.trans.opsisdis.trans_wo.urls import router as trans_wo
from apps.trans.opsisdis.trans_pm.urls import router as trans_pm
from apps.trans.opsisdis.trans_pm_detail.urls import router as trans_pm_detail
from apps.trans.opsisdis.trans_aset_mutasi.urls import router as trans_aset_mutasi


 
#fasop_scada
from apps.master.fasop.path1.urls import router as path1
from apps.master.fasop.path3.urls import router as path3
from apps.master.fasop.pm.urls import router as pm
from apps.master.fasop.master.urls import router as master
from apps.master.fasop.rtu.urls import router as rtu
from apps.master.fasop.point_type.urls import router as point_type
from apps.master.fasop.point_type_state.urls import router as point_type_state
from apps.master.fasop.telegram_bot.urls import router as telegram_bot
from apps.master.fasop.telegram_group.urls import router as telegram_group
from apps.master.fasop.telegram_log.urls import router as telegram_log
from apps.master.fasop.c_point.urls import router as c_point

# opsisdis master
from apps.master.opsisdis.jenis_penyebab_gangguan.urls import router as opsisdis_jenis_penyebab_gangguan
from apps.master.opsisdis.penyebab_gangguan.urls import router as opsisdis_penyebab_gangguan
from apps.master.opsisdis.frekuensi.urls import router as frekuensi
from apps.master.opsisdis.amr_customer.urls import router as amr_customer 
# master opsisdis - pm
from apps.master.opsisdis.pm.ref_hi.urls import router as ref_hi
from apps.master.opsisdis.pm.ref_pm.urls import router as ref_pm
from apps.master.opsisdis.pm.ref_pm_detail.urls import router as ref_pm_detail
from apps.master.opsisdis.pm.ref_pm_detail_logic.urls import router as ref_pm_detail_logic

from apps.master.opsisdis.wo.ref_wo_jenis.urls import router as ref_wo_jenis
from apps.master.opsisdis.wo.ref_wo_status.urls import router as ref_wo_status
from apps.master.opsisdis.ref_jenis_pekerjaan.urls import router as ref_jenis_pekerjaan

from apps.master.opsisdis.rekap_padam.ref_ep_fiohl.urls import router as ref_ep_fiohl
from apps.master.opsisdis.rekap_padam.ref_ep_indikasi.urls import router as ref_ep_indikasi
from apps.master.opsisdis.rekap_padam.ref_ep_petugas.urls import router as ref_ep_petugas
from apps.master.opsisdis.rekap_padam.ref_ep_rupiah.urls import router as ref_ep_rupiah
from apps.master.opsisdis.rekap_padam.ref_ep_cuaca.urls import router as ref_ep_cuaca
from apps.master.opsisdis.rekap_padam.ref_ep_penyebab_ggn.urls import router as ref_ep_penyebab_ggn
from apps.master.opsisdis.rekap_padam.ref_ep_fdir.urls import router as ref_ep_fdir

# opsisdis
from apps.opsisdis.telemetring.pembangkit.urls import router as opsisdis_telemetring_pembangkit
from apps.opsisdis.telemetring.trafo_gi_non_ktt.urls import router as opsisdis_telemetring_trafo_gi
from apps.opsisdis.telemetring.penyulang.urls import router as opsisdis_telemetring_penyulang
from apps.opsisdis.telemetring.zona.urls import router as opsisdis_telemetring_zona
from apps.opsisdis.telemetring.area.urls import router as opsisdis_telemetring_area
from apps.opsisdis.telemetring.wilayah.urls import router as opsisdis_telemetring_wilayah
from apps.opsisdis.telemetring.amr_energi.urls import router as opsisdis_telemetring_amr_energi
from apps.opsisdis.telemetring.amr_load_profile.urls import router as opsisdis_telemetring_amr_load_profile
from apps.opsisdis.frekuensi.scd_trans_frek_5m.urls import router as opsisdis_frekuensi_scd_trans_frek_5m
from apps.opsisdis.frekuensi.scd_trans_frek_his.urls import router as opsisdis_frekuensi_scd_trans_frek_his
from apps.opsisdis.frekuensi.scd_frek_rtl.urls import router as opsisdis_frekuensi_scd_trans_frek_rtl
from apps.opsisdis.frekuensi.scd_frek_th.urls import router as opsisdis_frekuensi_scd_trans_frek_th
from apps.opsisdis.frekuensi.backup_harian.urls import router as opsisdis_frekuensi_backup_harian

#opsis laporan beban
from apps.opsisdis.laporan_beban.trans_tm_trafo_gi_jam.urls import router as trans_tm_trafo_gi_jam
from apps.opsisdis.laporan_beban.trans_tm_trafo_gi_hari.urls import router as trans_tm_trafo_gi_hari
from apps.opsisdis.laporan_beban.trans_tm_trafo_gi_bulan.urls import router as trans_tm_trafo_gi_bulan
from apps.opsisdis.laporan_beban.trans_tm_trafo_gi_tahun.urls import router as trans_tm_trafo_gi_tahun
from apps.opsisdis.laporan_beban.trans_tm_penyulang_jam.urls import router as trans_tm_penyulang_jam
from apps.opsisdis.laporan_beban.trans_tm_penyulang_hari.urls import router as trans_tm_penyulang_hari
from apps.opsisdis.laporan_beban.trans_tm_penyulang_bulan.urls import router as trans_tm_penyulang_bulan
from apps.opsisdis.laporan_beban.trans_tm_penyulang_tahun.urls import router as trans_tm_penyulang_tahun
from apps.opsisdis.laporan_beban.trans_tm_up3.urls import router as trans_tm_up3_jam
from apps.opsisdis.laporan_beban.trans_tm_up3_hari.urls import router as trans_tm_up3_hari
from apps.opsisdis.laporan_beban.trans_tm_up3_bulan.urls import router as trans_tm_up3_bulan
from apps.opsisdis.laporan_beban.trans_tm_up3_tahun.urls import router as trans_tm_up3_tahun
from apps.opsisdis.laporan_beban.trans_tm_up2b_jam.urls import router as trans_tm_up2b_jam
from apps.opsisdis.laporan_beban.trans_tm_up2b_hari.urls import router as trans_tm_up2b_hari
from apps.opsisdis.laporan_beban.trans_tm_up2b_bulan.urls import router as trans_tm_up2b_bulan
from apps.opsisdis.laporan_beban.trans_tm_up2b_tahun.urls import router as trans_tm_up2b_tahun
from apps.opsisdis.laporan_beban.trans_tm_uid_jam.urls import router as trans_tm_uid_jam
from apps.opsisdis.laporan_beban.trans_tm_uid_hari.urls import router as trans_tm_uid_hari
from apps.opsisdis.laporan_beban.trans_tm_uid_bulan.urls import router as trans_tm_uid_bulan
from apps.opsisdis.laporan_beban.trans_tm_uid_tahun.urls import router as trans_tm_uid_tahun
from apps.opsisdis.laporan_beban.trans_tm_subsistem_jam.urls import router as trans_tm_subsistem_jam
from apps.opsisdis.laporan_beban.trans_tm_subsistem_hari.urls import router as trans_tm_subsistem_hari
from apps.opsisdis.laporan_beban.trans_tm_subsistem_bulan.urls import router as trans_tm_subsistem_bulan
from apps.opsisdis.laporan_beban.trans_tm_subsistem_tahun.urls import router as trans_tm_subsistem_tahun

#JADWAL PEMELIHARAAN
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har.urls import router as trans_jadwal_har
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har_dok.urls import router as trans_jadwal_har_dok
from apps.opsisdis.jadwal_pemeliharaan.trans_jadwal_har_gardu.urls import router as trans_jadwal_har_gardu

from apps.opsisdis.urf.penyulang_urf.urls import router as penyulang_urf
# external
from apps.external.ext_module.urls import router as ext_module
from apps.external.ext_user_token.urls import router as ext_user_token
from apps.external.ext_user_token_role.urls import router as ext_user_token_role

#users 
from apps.users.urls import router as users

#roles 
from apps.roles.urls import router as roles

#menu 
from apps.menu.urls import router as menu

#fasop HISTORI 
from apps.fasop.histori.scd_his_analog.urls import router as his_analog
from apps.fasop.histori.scd_his_analog_30m.urls import router as his_analog_30m
from apps.fasop.histori.scd_his_digital.urls import router as his_digital
from apps.fasop.histori.scd_his_rtu.urls import router as his_rtu
from apps.fasop.histori.scd_his_master.urls import router as his_master
# from apps.fasop.histori.scd_his_message.urls import router as his_message
from apps.fasop.histori.scd_his_trip.urls import router as his_trip
from apps.fasop.histori.scd_his_rc.urls import router as his_rc

#FASOP KINERJA
from apps.fasop.kinerja.scd_kin_digital_bulan.urls import router as kin_digital_bulan
from apps.fasop.kinerja.scd_kin_digital_harian.urls import router as kin_digital_harian
from apps.fasop.kinerja.scd_kin_rtu_bulan.urls import router as kin_rtu_bulan
from apps.fasop.kinerja.scd_kin_rtu_harian.urls import router as kin_rtu_harian
from apps.fasop.kinerja.scd_kin_analog_bulan.urls import router as kin_analog_bulan
from apps.fasop.kinerja.scd_kin_analog_harian.urls import router as kin_analog_harian
from apps.fasop.kinerja.scd_kin_master_bulan.urls import router as kin_master_bulan
from apps.fasop.kinerja.scd_kin_master_harian.urls import router as kin_master_harian

#FASOP REALTIME
from apps.fasop.realtime.scd_analog_rtl.urls import router as rtl_analog
from apps.fasop.realtime.scd_digital_rtl.urls import router as rtl_digital
from apps.fasop.realtime.scd_master_rtl.urls import router as rtl_master
from apps.fasop.realtime.scd_rtu_rtl.urls import router as rtl_rtu

#APKT
from apps.apkt.apkt_trans_jar.urls import router as apkt_trans_jar
from apps.apkt.apkt_trans_jar_det.urls import router as apkt_trans_jar_det
from apps.apkt.apkt_trans_log.urls import router as apkt_trans_log

#Working Permit
# from apps.working_permit.wp_bagian.urls import router as wp_bagian
from apps.working_permit.wp_hirarc.urls import router as wp_hirarc
from apps.working_permit.wp_hirarc_detail.urls import router as wp_hirarc_detail
from apps.working_permit.wp_master_sop_jsa.urls import router as wp_master_sop_jsa
from apps.working_permit.wp_qrc.urls import router as wp_qrc
from apps.working_permit.wp_qrc_detail.urls import router as wp_qrc_detail 
from apps.working_permit.wp_qrc_tmp.urls import router as wp_qrc_tmp  
from apps.working_permit.wp_ttd_online.urls import router as wp_ttd_online
from apps.working_permit.wp_online.urls import router as wp_online
from apps.working_permit.wp_online_pekerja.urls import router as wp_online_pekerja
from apps.working_permit.wp_aproval_ttd.urls import router as wp_aproval_ttd
from apps.working_permit.wp_dok.urls import router as wp_dok
from apps.working_permit.wp_sop_perlengkapan.urls import router as wp_sop_perlengkapan

#opsisdis sld
from apps.opsisdis.sld.daf_sld_gi.urls import router as daf_sld_gi

#opsisdis rekap padam
from apps.opsisdis.rekap_padam.trans_ep.urls import router as trans_ep
from apps.opsisdis.rekap_padam.trans_ep_laporan.urls import router as trans_ep_laporan
from apps.opsisdis.rekap_padam.trans_ep_peralatan.urls import router as trans_ep_peralatan
from apps.opsisdis.rekap_padam.trans_ep_section.urls import router as trans_ep_section

#histori
from apps.histori.users_his_password.urls import router as user_his_password

#fasop - laporan scada- realtime scada
from apps.fasop.realtime_scd.urls import router as realtime_scd
from apps.fasop.soe_alarm_proteksi.urls import router as soe_alarm_proteksi
from apps.fasop.histori_rc.urls import router as histori_rc
from apps.fasop.kinerja_rc.urls import router as kinerja_rc
from apps.fasop.histori_peralatan_scd.urls import router as histori_peralatan_scd
from apps.fasop.kinerja_peralatan_scd.urls import router as kinerja_peralatan_scd

# dashboard
from apps.dashboard.kinerja_scd.urls import router as dashboard_kinerja_peralatan_scd

from apps.latihan.latihan1.urls import router as latihan1

router = routers.DefaultRouter(trailing_slash=False)
#tests
router.extend(send_mail)
router.extend(test_rekap_padam)

#master jaringan
router.extend(ref_jenis_lokasi)
router.extend(ref_jenis_pembangkit)
router.extend(ref_lokasi)
router.extend(tree_jaringan)
router.extend(ref_lokasi_gd)
router.extend(ref_pemilik_jaringan)

#MASTER WILAYAH
router.extend(ref_province)
router.extend(ref_regency)
router.extend(ref_district)

#master asetwilayah
router.extend(ref_aset)
router.extend(ref_aset_doc)
router.extend(ref_aset_ex_atr)
router.extend(ref_aset_ext_atr)
router.extend(ref_aset_jenis)
router.extend(ref_asetm_manufaktur)
router.extend(ref_aset_lantai)
router.extend(ref_aset_ruangan)
router.extend(ref_aset_rak)
router.extend(ref_aset_kondisi)
router.extend(ref_aset_level)
router.extend(ref_aset_status)
router.extend(ref_aset_jenis_mutasi)

#master pm
router.extend(ref_hi)
router.extend(ref_pm)
router.extend(ref_pm_detail)
router.extend(ref_pm_detail_logic)

#master wo
router.extend(ref_wo_jenis)
router.extend(ref_wo_status)

#master wr
router.extend(ref_wr_status)

# master pegawai
router.extend(pegawai_departemen)
router.extend(pegawai_jabatan)
router.extend(pegawai_perusahaan)
router.extend(ref_pegawai)
router.extend(ref_regu_petugas)

#application_setting
router.extend(application_setting)

#Management Upload
router.extend(management_upload)
router.extend(unit_pembangkit)
router.extend(pembangkit)
router.extend(gardu_induk)
router.extend(trafo_gi)
router.extend(penyulang)
router.extend(zona)
router.extend(section)
router.extend(segment)
router.extend(gardu_distribusi)
router.extend(trafo_gd)
router.extend(gardu_hubung)
router.extend(kantor)

#Working Management
router.extend(pertanyaan_qrc)
router.extend(risk_point_qrc)
router.extend(larangan_tanggung_jawab_mitra)
router.extend(approval_management_wp)
router.extend(wp_bagian)
router.extend(ref_kel_keselamatan)
router.extend(ref_kel_pekerjaan)

#trans opsisdis
router.extend(trans_pm_jenis_doc)
router.extend(trans_wo)
router.extend(trans_wo_log_status)
router.extend(trans_pm)
router.extend(trans_pm_detail)
router.extend(trans_aset_mutasi)

# FASOP SCADA
router.extend(path1)
router.extend(path3)
router.extend(pm)
router.extend(master)
router.extend(rtu)
router.extend(point_type)
router.extend(point_type_state)
router.extend(telegram_bot)
router.extend(telegram_group)
router.extend(telegram_log)
router.extend(c_point)

# opsisdis master
router.extend(opsisdis_jenis_penyebab_gangguan)
router.extend(opsisdis_penyebab_gangguan)
router.extend(frekuensi)
router.extend(ref_jenis_pekerjaan)

router.extend(ref_ep_fiohl)
router.extend(ref_ep_indikasi)
router.extend(ref_ep_petugas)
router.extend(ref_ep_rupiah)
router.extend(ref_ep_cuaca)
router.extend(ref_ep_penyebab_ggn)
router.extend(ref_ep_fdir)
# opsisdis 
router.extend(opsisdis_telemetring_pembangkit)
router.extend(opsisdis_telemetring_trafo_gi)
router.extend(opsisdis_telemetring_penyulang)
router.extend(opsisdis_telemetring_zona)
router.extend(opsisdis_telemetring_area)
router.extend(opsisdis_telemetring_wilayah)
router.extend(amr_customer)
router.extend(opsisdis_telemetring_amr_energi)
router.extend(opsisdis_telemetring_amr_load_profile)
router.extend(opsisdis_frekuensi_scd_trans_frek_5m)
router.extend(opsisdis_frekuensi_scd_trans_frek_his)
router.extend(opsisdis_frekuensi_scd_trans_frek_rtl)
router.extend(opsisdis_frekuensi_scd_trans_frek_th)
router.extend(opsisdis_frekuensi_backup_harian)

#opsis laporan beban
router.extend(trans_tm_trafo_gi_jam)
router.extend(trans_tm_trafo_gi_hari)
router.extend(trans_tm_trafo_gi_bulan)
router.extend(trans_tm_trafo_gi_tahun)
router.extend(trans_tm_penyulang_jam)
router.extend(trans_tm_penyulang_hari)
router.extend(trans_tm_penyulang_bulan)
router.extend(trans_tm_penyulang_tahun)
router.extend(trans_tm_up3_jam)
router.extend(trans_tm_up3_hari)
router.extend(trans_tm_up3_bulan)
router.extend(trans_tm_up3_tahun)
router.extend(trans_tm_up2b_jam)
router.extend(trans_tm_up2b_hari)
router.extend(trans_tm_up2b_bulan)
router.extend(trans_tm_up2b_tahun)
router.extend(trans_tm_uid_jam)
router.extend(trans_tm_uid_hari)
router.extend(trans_tm_uid_bulan)
router.extend(trans_tm_uid_tahun)
router.extend(trans_tm_subsistem_jam)
router.extend(trans_tm_subsistem_hari)
router.extend(trans_tm_subsistem_bulan)
router.extend(trans_tm_subsistem_tahun)

#JADWAL PEMELIHARAAN
router.extend(trans_jadwal_har)
router.extend(trans_jadwal_har_dok)
router.extend(trans_jadwal_har_gardu)
#urf
router.extend(penyulang_urf)
# external
router.extend(ext_module)
router.extend(ext_user_token)
router.extend(ext_user_token_role)

#users 
router.extend(users)

#roles 
router.extend(roles)

#menu 
router.extend(menu)

#fasop trans 
router.extend(his_analog)
router.extend(his_analog_30m)
router.extend(his_digital)
router.extend(his_rtu)
router.extend(his_master)
# router.extend(his_message)
router.extend(his_trip)
router.extend(his_rc)

#fasop kinerja

router.extend(kin_digital_bulan)
router.extend(kin_digital_harian)
router.extend(kin_rtu_bulan)
router.extend(kin_rtu_harian)
router.extend(kin_analog_bulan)
router.extend(kin_analog_harian)
router.extend(kin_master_bulan)
router.extend(kin_master_harian)

#fasop realtime
router.extend(rtl_analog)
router.extend(rtl_digital)
router.extend(rtl_master)
router.extend(rtl_rtu)

#apkt
router.extend(apkt_trans_jar)
router.extend(apkt_trans_jar_det)
router.extend(apkt_trans_log)

#working permit 
router.extend(wp_hirarc)
router.extend(wp_hirarc_detail)
router.extend(wp_master_sop_jsa)
router.extend(wp_qrc)
router.extend(wp_qrc_detail) 
router.extend(wp_qrc_tmp)  
router.extend(wp_ttd_online)
router.extend(wp_online)
router.extend(wp_online_pekerja)
router.extend(wp_aproval_ttd)
router.extend(wp_dok)
router.extend(wp_sop_perlengkapan)
#OPSISDIS SLD
router.extend(daf_sld_gi)

#histori
router.extend(user_his_password)
#fasop - laporan scada - realtime scada
router.extend(realtime_scd)
router.extend(soe_alarm_proteksi) 
router.extend(histori_rc) 
router.extend(kinerja_rc) 
router.extend(histori_peralatan_scd) 
router.extend(kinerja_peralatan_scd) 
#opsisdis rekap padam
router.extend(trans_ep)
router.extend(trans_ep_laporan)
router.extend(trans_ep_peralatan)
router.extend(trans_ep_section)


# dashboard 
router.extend(dashboard_kinerja_peralatan_scd) 