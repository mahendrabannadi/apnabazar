from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print("Customer",request.session.get('customer'))
        print("middleware")
        returnUrl = request.META['PATH_INFO']
        print("Path info",request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware
