local function status_line()
  local mode = "  %-5{%v:lua.string.upper(v:lua.vim.fn.mode())%}"
  local file_name = "%f"
  local modified = " %-m "
  local path_file = "%F"
  local buf_nr = " [%n] "
  local file_type = " %y"
  local right_align = "%="
  local line_no = "%10([%l: %c : %L%)]"
  local pct_thru_file = "%5p%%  "

  return string.format(
    "%s%s%s%s%s%s%s%s",
    mode,
    file_name,
    buf_nr,
    file_type,
    modified,
    right_align,
    line_no,
    pct_thru_file
  )
end

vim.opt.statusline = status_line()

