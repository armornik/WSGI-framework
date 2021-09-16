from views import Index, About

# Set of bindings: path-controller
routes = {
    '/': Index(),
    '/about/': About(),
}
