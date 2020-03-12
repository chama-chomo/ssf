# SSF - one more way to interact with Foreman

* It can list only devices belonging to your team
* It can connect you to a device using SSH and default root password (DEV env)
* It can connect you to a base os of the device using serial console managed by
  HP ILO ('c' option)
* It can serve you ILO web link of the particular machine ('i' option) directly
  in your web browser

```
   ---------------------------------------------------------------------------------------------
   +++ Foreman API terminal tool for getting a list of objects and accessing them on request +++
   ---------------------------------------------------------------------------------------------
    
        Total devices found:  5 

-----------------------------------------------------------------------------------------------------------------------------------------------------
 # | DEVICE NAME         | IP/ILO IP            | OS/MODEL        | STATUS          | OWNER/GROUP          | COMMENT                                 
-----------------------------------------------------------------------------------------------------------------------------------------------------
 1 | -ffff-000000029042  | IP:     10.10.29.42  | WPH_main 2.0.0  | OK              | Matej Soroka         | WPHT-42446 Install V                    
   |                     | ILO-IP: 10.10.29.43  | SKU1 Edge       | Installed       | Scarabs              | elero and MinIO                         
-----------------------------------------------------------------------------------------------------------------------------------------------------
 2 | -ffff-000000029046  | IP:     10.10.29.46  | WPH_main 2.0.0  | OK              | Marek Vaculovic      | RAM of SKU3                             
   |                     | ILO-IP: 10.10.29.47  | SKU2 Edge       | Installed       | Scarabs              |                                         
-----------------------------------------------------------------------------------------------------------------------------------------------------
 3 | -ffff-000000029054  | IP:     10.10.29.54  | WPH_main 1.9    | Error           | Martin Ciganik       | mci                                     
   |                     | ILO-IP: 10.10.29.55  | SKU3 Edge       | Token expired   | Scarabs              |                                         
-----------------------------------------------------------------------------------------------------------------------------------------------------
 4 | -ffff-000000029094  | IP:     10.10.29.94  | WPH_main 2.0.0  | OK              | Marek Vaculovic      | Machine in Server ro                    
   |                     | ILO-IP: 10.10.29.95  | SKU1            | Installed       | Scarabs              | om                                      
-----------------------------------------------------------------------------------------------------------------------------------------------------
 5 | -ffff-010010029066  | IP:     10.10.29.222 | WPH_main 1.9    | OK              | Martin Ciganik       | [WPHT-42599] Full Ba                    
   |                     | ILO-IP: 10.10.29.208 | SKU2            | Installed       | Scarabs              | ckup Data Size Analysis                 
-----------------------------------------------------------------------------------------------------------------------------------------------------

For specifying a host that you want to access using ssh, type number as per index.
        For accessing ILO using webbrowser prepend number with letter [i]
        For accessing ILO console prepend number with letter          [c]
Host ID: 

```


