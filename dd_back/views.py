from pyramid.view import view_config
from dd_back.merger import Merger

@view_config(route_name='dbmerge', renderer='json')
def db_merge_view(request):
    request.response.headerlist.extend([('Access-Control-Allow-Origin', '*'),])
    args = request.params['args']
    merger = Merger(args)
    return merger.merge()
    return {'project':'dd_back'}
