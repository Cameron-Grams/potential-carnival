vim.g.mapleader = "\\"

-- file tree
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

-- features
vim.cmd("set number relativenumber")
vim.cmd("set cursorline")

-- key bindings
vim.cmd(":inoremap jf <esc>")
vim.cmd(":inoremap fj <esc>")
vim.cmd("nmap <leader>c :set cursorcolumn!<CR>")
vim.cmd(":map mm <Esc>")
vim.cmd(":map <space> viw")
vim.cmd("hi Function ctermfg=DarkBlue")
