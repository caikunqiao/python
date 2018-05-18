mix = ('mushrooms', 'green peppers', 'extra cheese')
#mix = []
requested_mixture = ['extra cheese','alcohol','green peppers']
if mix:
    for requested_mix in requested_mixture:
        if requested_mix in mix: 
            if requested_mix == "green peppers":
                print("sorry we r out of green peppers.")
            else:
                print("Adding " + requested_mix + ".")
        else:
            print("Sorry, we don't have " + requested_mix + ".")
    print("Finished making your pizza!")        
else:
    print("Are you sure you want a plain pizza?")

