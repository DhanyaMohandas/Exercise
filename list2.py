months=['Jan','Feb','Mar','Apr']
months.append ('May')
months.append ('July')
print 'Adding May & July', months 
months.insert (5,'Jun')
print 'Print current list',months
print 'Index of May is:',months.index ('May')
months.remove ('Jun')
print 'Jun is removed.The new list is',months
months.sort ()
print 'Sorted list is',months
months.reverse ()
print 'Reverse list is',months
