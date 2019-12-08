import neovim
# from .lib import seeker


@neovim.plugin
class Konbu(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("KonbuP", sync=True)
    def konbu_p(self):
        self.nvim.out_write('KonbuP' + '\n')
