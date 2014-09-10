#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import csv
import os.path, time

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")


print """
<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
    var data = google.visualization.arrayToDataTable([
"""

print """
     ['DatastoreName', 'TotalSpaceGB', 'UsedSpaceGB', 'ProvisionedSpaceGB', 'FreeSpaceGB'],
"""
AllTotalSpaceGB = 0
AllUsedSpaceGB = 0
AllProvisionedSpaceGB = 0
AllFreeSpaceGB = 0
with open('../datastores.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',', )
    for row in reader:
        Datacenter = row[0]
	if Datacenter != "Datacenter":
            NumVMHost = int(row[8])
            Type = row[3]
            if NumVMHost > 2 and Type == 'VMFS':
                DatastoreName = row[1]
                TotalSpaceGB = int(row[2])
                AllTotalSpaceGB = int(AllTotalSpaceGB) + int(TotalSpaceGB)
                UsedSpaceGB = int(row[4])
                AllUsedSpaceGB = int(AllUsedSpaceGB) + int(UsedSpaceGB)
                ProvisionedSpaceGB = int(row[5])
                AllProvisionedSpaceGB = int(AllProvisionedSpaceGB) + int(ProvisionedSpaceGB)
                FreeSpaceGB = int(row[6])
                NumVM = int(row[7])
                AllFreeSpaceGB = int(AllFreeSpaceGB) + int(FreeSpaceGB)

                print "     ['["+Datacenter+"] "+str(DatastoreName)+"',"+str(TotalSpaceGB)+","+str(UsedSpaceGB)+","+str(ProvisionedSpaceGB)+","+str(FreeSpaceGB)+"],"

print """
 ]);
        var options = {
          legend: { position: 'top', alignment: 'start' },
          title: 'iSCSI Share Storages',
          chartArea:{left:300,top:70},
        };

        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
    </script>

  </head>
  <body>
"""
print "    <b>Last Update:</b> %s" % time.ctime(os.path.getmtime('../datastores.csv'))+"<hr>"
print "    <b>Total: <tt>"+str(AllTotalSpaceGB)+"GB</tt> "
print "    <b>Used: <tt>"+str(AllUsedSpaceGB)+"GB</tt> "
print "    <b>Free: <tt>"+str(AllFreeSpaceGB)+"GB</tt> "
print "    <b>Provisioned: <tt>"+str(AllProvisionedSpaceGB)+"GB</tt></b>"
print """
    <div id="chart_div" style="width: 1700px; height: 1000px;"></div>
  </body>
</html>
"""
