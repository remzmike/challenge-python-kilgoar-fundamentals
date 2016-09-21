-- lua 5.1
-- m.k.

-- 15. Write the function from question 12 in a different language.

local array = {1, 2, 3, 4, 5, 6, 7, 8, 9}

function binary_search(A, x, lo, hi)
    while lo < hi do
        local i = math.floor((lo+hi)/2)
        if A[i+1] < x then
            lo = i + 1
        elseif A[i+1] > x then
            hi = i
        else
            return i
        end
    end
    return -1
end

local lo = 0
local hi = #array-1
assert(binary_search(array, 13, lo, hi)==-1)
assert(binary_search(array, 1, lo, hi)==0)
assert(binary_search(array, 1, lo+1, hi)==-1)
assert(binary_search(array, 8, lo, hi)==7)
assert(binary_search(array, 8, lo, 8)==7)
assert(binary_search(array, 8, lo, 7)==-1)
assert(binary_search(array, -2, lo, hi)==-1)

-- 16. Write the program from question 14 in a different language (it can
--     be the same language you used for #15, but it doesn't have to be).

function get_line(fpath, n)
    local f = assert(io.open(fpath, 'rb'))
    local line_count = 0
    local line = f:read()
    local result
    while line do
        line_count = line_count + 1
        if line_count == n then
            result = line
            break
        end
        line = f:read()
    end
    assert(f:close())
    return result
end

-- print( get_line('c:/tmp.py',18) )
print(get_line(arg[1], tonumber(arg[2])))