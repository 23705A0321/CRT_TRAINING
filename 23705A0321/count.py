def function(count):
    if count == 6:
        return
    print(count)
    count = count + 1
    function(count)
function(1)