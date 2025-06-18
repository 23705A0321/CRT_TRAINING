def function(count):
    if count == 10:
        return
    count = count + 1
    function(count)
    print(count)        #stack element
function(1)