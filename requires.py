from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes
from charms.reactive import is_state


class CephClient(RelationBase):
    scope = scopes.GLOBAL
    auto_accessors = ['cephx_key']

    @hook('{requires:backup}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
        if self.directories():
            self.set_state('{relation_name}.available')

    @hook('{requires:backup}-relation-{broken,departed}')
    def broken(self):
        if is_state('{relation_name}.available'):
            self.remove_state('{relation_name}.available')
