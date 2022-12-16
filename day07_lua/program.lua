prof = require 'ProFi'

function main()
    print("Day 7")

    solve("sample.txt")
    solve("real_input.txt")
end

function solve(filename)
    print("\n\n## SOLVING ",filename,"\n")
    io.flush()

    local dirsizes = getdirsizes(filename)
    print(tableCount(dirsizes), "directories")

    local smallEnoughDirs = withoutLargeDirs(dirsizes, 100000)
    print(tableCount(smallEnoughDirs), "small directories")

    local sum = tableSum(smallEnoughDirs)
    print(sum..":", "sum of the small directories files' sizes")
end

function getdirsizes(filename)
    local state = {
        result = {},
        pwd = ""
    }

    i = 1
    for line in io.lines(filename) do
        runline(state, line)
    end

    return state.result
end

-- Handles `line` and updates `state` accordingly
function runline(state, line)
    if line:startswith("$ cd") then
        local arg = line:gsub("$ cd ", "")
        changedirectory(state, arg)
    elseif line:startswith("$ ls") or line:startswith("dir") then
        return
    else
        local arg = line:match("^%d+")
        addfilesize(state, arg)
    end
end

-- Change the current directory
function changedirectory(state, arg)
    if arg == "/" then
        state.pwd = arg
        return
    end

    if arg == ".." then
        state.pwd = state.pwd:withoutLastDir()
        return
    end

    state.pwd = state.pwd .. "/" .. arg
    collapseSlashes(state)
end

function collapseSlashes(state)
    state.pwd = state.pwd:gsub("//", "/")
end

-- Add the given file size to every relevant directory total in `state`
function addfilesize(state, arg)
    dir = state.pwd
    repeat
        if not state.result[dir] then
            state.result[dir] = 0
        end

        assert(type(state.result[dir]) == "number")
        assert(type(tonumber(arg)) == "number", arg .. " is a number")

        state.result[dir] = state.result[dir] + tonumber(arg)

        dir = dir:withoutLastDir()
    until not dir or #dir == 0
end

function withoutLargeDirs(dirsTable, maxSize)
    copy = {}
    for k,v in pairs(dirsTable) do
        if v <= maxSize then
            copy[k] = v
        end
    end
    return copy
end

-- TABLE HELPERS

function tableCount(t)
    local n = 0
    for _ in pairs(t) do
        n = n + 1
    end
    return n
end

function tableSum(t)
    local sum = 0
    for _,v in pairs(t) do
        sum = sum + v
    end
    return sum
end

-- STRING METHODS

meta = getmetatable("")
function meta.__index.startswith(s, prefix)
    local f = s:find(prefix, 1, true)
    return f and f == 1
end

function meta.__index.withoutLastDir(s)
    if #s == 1 then
        -- false is a flag value that indicates
        -- there are no more dirs to remove.
        return false
    end

    new = s:gsub("/%w+$", "", 1)

    if #new == 0 then
        -- special case: we're at the root directory
        new = "/"
    end

    return new
end

main()
