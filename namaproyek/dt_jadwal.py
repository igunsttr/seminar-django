from ajax_datatable.views import AjaxDatatableView
from .models import Jadwal
class Jadwalku(AjaxDatatableView):
    model = Jadwal
    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),        
        {'name': 'no', 'title':'No','visible': True, 'searchable': False,'autofilter': False,},
        {'name': 'id_matkul', 'foreign_field':'id_matkul__nama','title':'Nama Matkul','visible': True, 'searchable': True,'autofilter': True,},
        {'name': 'id_dosen', 'foreign_field':'id_dosen__nama','title':'Dosen','visible': True, 'searchable': True,'autofilter': True,},
        {'name': 'id_ruang', 'foreign_field':'id_ruang__nama','title':'Ruang','visible': True, 'searchable': True,'autofilter': True,},
        {'name': 'id_jurusan','foreign_field':'id_jurusan__nama', 'title':'Jurusan','visible': True, 'searchable': True,'autofilter': True,},
        {'name': 'waktu_1','title':'Waktu Awal','visible': True, 'searchable': True,},
        {'name': 'waktu_2','title':'Waktu Akhir','visible': True, 'searchable': True,},

    ]
    """   def get_initial_queryset(self, request=None):

        def get_numeric_param(key):
            try:
                value = int(request.POST.get(key))
            except:
                value = None
            return value

        queryset = super().get_initial_queryset(request=request)

        #date_from = request.POST.get('date_from')
        #date_to =  request.POST.get('date_to')

        return queryset """