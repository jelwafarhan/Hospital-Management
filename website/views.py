from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import hadmin,doctor,billingadmin,patient,department,medicine,pprescription,booking,purchase
from django.forms.models import model_to_dict
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from django.core.mail import send_mail
# Create your views here.

def home (request): 
    dep = department.objects.all()   
    return render(request,"index.html",{"departments":dep})

def patientdirectreg (request):    
    return render(request,"form/register/patientdirectreg.html")

def patientdirectregsave (request):
    pdrs=patient()
    pdrs.name=request.POST.get("name")
    pdrs.password=request.POST.get("password")
    pdrs.age=request.POST.get("age")
    pdrs.email=request.POST.get("email")
    pdrs.gender=request.POST.get("gender")
    pdrs.number=request.POST.get("number")
    pdrs.img=request.FILES["img"]
    pdrs.save()
    return home(request)


#login

def doctorlogin (request): 
    return render(request,"login/doctorlogin.html")

def doctorcheck (request):      
    dcheck= len(doctor.objects.filter(email=request.POST.get("email"),password=request.POST.get("password")))
    if dcheck>0:        
        dload=doctor.objects.filter(email=request.POST.get("email"),password=request.POST.get("password"))
        for dc in dload:
            request.session["doctor_id"] = dc.id
        return doctordashboard(request)
    else:
        at='incorrect mail id or password, check and try again' 
        data=1     
        return render(request,"login/doctorlogin.html",{"alert":at,"data":data})
    return render(request,"login/doctorlogin.html")


def patientlogin (request): 
    return render(request,"login/patientlogin.html")

def patientcheck (request):      
    pcheck= len(patient.objects.filter(email=request.POST.get("email"),password=request.POST.get("password")))
    if pcheck>0:        
        pload=patient.objects.filter(email=request.POST.get("email"),password=request.POST.get("password"))
        for pc in pload:
            request.session["patient_id"] = pc.id
        return patientdashboard(request)
    else:
        at='incorrect mail id or password, check and try again' 
        data=1     
        return render(request,"login/patientlogin.html",{"alert":at,"data":data})
    return render(request,"login/patientlogin.html")


def hadminlogin (request): 
    return render(request,"login/hadminlogin.html")

def hadmincheck (request):      
    hcheck= len(hadmin.objects.filter(email=request.POST.get("email"),password=request.POST.get("password")))
    if hcheck>0:        
        hload=hadmin.objects.filter(email=request.POST.get("email"),password=request.POST.get("password"))
        for hac in hload:
            request.session["hadmin_id"] = hac.id
        return hadmindashboard (request)
    else:
        at='incorrect mail id or password, check and try again' 
        data=1     
        return render(request,"login/hadminlogin.html",{"alert":at,"data":data})
    return render(request,"login/hadminlogin.html")


def billingadminlogin (request): 
    return render(request,"login/billingadminlogin.html")

def billingadmincheck (request):      
    bcheck= len(billingadmin.objects.filter(email=request.POST.get("email"),password=request.POST.get("password")))
    if bcheck>0:        
        bload=billingadmin.objects.filter(email=request.POST.get("email"),password=request.POST.get("password"))
        for bc in bload:
            request.session["billingadmin_id"] = bc.id
            
        return billingadmindashboard(request)
    else:
        at='incorrect mail id or password, check and try again' 
        data=1     
        return render(request,"login/billingadminlogin.html",{"alert":at,"data":data})
    return render(request,"login/billingadminlogin.html")



#doctor

def doctordashboard (request): 
    dload=doctor.objects.filter(id=request.session["doctor_id"])
    bdl= booking.objects.filter(doctor__id=request.session["doctor_id"])  
    print(bdl)     
    return render(request,"dashboard/doctordashboard.html",{"doctordetials":dload,"bookinglists":bdl})

def doctorprofile (request): 
    dload=doctor.objects.filter(id=request.session["doctor_id"])       
    return render(request,"profile/doctorprofile.html",{"doctordetials":dload})

def patientlist (request): 
    dload=doctor.objects.filter(id=request.session["doctor_id"])
    pl=patient.objects.all()
    return render(request,"list/patientlist.html",{"doctordetials":dload,"patientlists":pl})

def medicinelist (request): 
    dload=doctor.objects.filter(id=request.session["doctor_id"])
    ml=medicine.objects.all()
    return render(request,"list/medicinelist.html",{"doctordetials":dload,"medicinelists":ml})

def prescription (request): 
    pl=patient.objects.all()
    ml=medicine.objects.all()
    dload=doctor.objects.filter(id=request.session["doctor_id"])
    return render(request,"form/prescription.html",{"doctordetials":dload,"patientlists":pl,"medicinelists":ml})

def prescriptionsave (request): 
    ps=pprescription()
    ps.patientname=get_object_or_404(patient,pk=request.POST.get("patient"))
    ps.medicinename= get_object_or_404(medicine,pk=request.POST.get("medicine"))
    ps.quantity=request.POST.get("quantity")
    ps.save()    
    return prescription(request)

def dbookinglist (request):    
    bol=booking.objects.filter(doctor__id=request.session["doctor_id"])
    dload=doctor.objects.filter(id=request.session["doctor_id"])
    return render(request,"list/dbookinglist.html",{"doctordetials":dload,"bookinglists":bol})


#patient


def patientdashboard (request): 
    pload=patient.objects.filter(id=request.session["patient_id"])
    bpl= booking.objects.filter(patient__id=request.session["patient_id"])   
    return render(request,"dashboard/patientdashboard.html",{"patientdetials":pload,"bookinglists":bpl})

def patientprofile (request): 
    pload=patient.objects.filter(id=request.session["patient_id"])    
    return render(request,"profile/patientprofile.html",{"patientdetials":pload})

def bookingpage (request): 
    dl=doctor.objects.all()
    pload=patient.objects.filter(id=request.session["patient_id"])    
    return render(request,"form/bookingpagecopy.html",{"patientdetials":pload,"doctorlists":dl})

def bookinglist (request):
    bpl= booking.objects.filter(patient__id=request.session["patient_id"])   
    pload=patient.objects.filter(id=request.session["patient_id"])    
    return render(request,"list/bookinglist.html",{"patientdetials":pload,"bookinglists":bpl})

def bookingsave(request):
    if request.method == 'POST':
        # Get the submitted date, time interval, doctor, and patient
        selected_date = request.POST.get("date")
        selected_time_interval = request.POST.get("time")
        selected_doctor_id = request.POST.get("doctor")
        selected_patient_id = request.POST.get("patient")

        # Split the time interval into start and end times
        start_time, end_time = selected_time_interval.split('-')

        # Check if the selected doctor and time slot are already booked
        existing_booking = booking.objects.filter(
            doctor_id=selected_doctor_id,
            date=selected_date,
            start_time__lt=end_time,  # Checking if start time overlaps
            end_time__gt=start_time   # Checking if end time overlaps
        ).exists()

        if existing_booking:
            messages.error(request, 'This time slot is already booked for the selected doctor.')
            return redirect('bookingpage')

        # Check how many bookings the patient has for this doctor on the selected date
        booking_count = booking.objects.filter(
            doctor_id=selected_doctor_id,
            date=selected_date
        ).count()

        if booking_count >= 10:
            messages.error(request, 'You have reached the maximum of 10 bookings for this doctor today.')
            return redirect('bookingpage')

        # Save the booking with the start time
        bos = booking()
        bos.patient = get_object_or_404(patient, pk=selected_patient_id)
        bos.doctor = get_object_or_404(doctor, pk=selected_doctor_id)
        bos.date = selected_date
        bos.start_time = start_time  # Save the start time of the interval
        bos.end_time = end_time  # Save the start time of the interval
        bos.save()

        patient_email = bos.patient.email
        doctor_name = bos.doctor.name 

        send_mail(
            'Booking Confirmed',
            f'Your appointment with. {doctor_name} on {selected_date} at {selected_time_interval} has been confirmed.',
            'your-email@gamil.com',
            [patient_email],
            fail_silently=  False,
        )

        messages.success(request, 'Booking successful.')
        return redirect('bookingpage')

    messages.error(request, 'Invalid request.')
    return redirect('bookingpage')


def check_slot_availability(request):
    doctor_id = request.GET.get('doctor_id')
    date = request.GET.get('date')
    time_interval = request.GET.get('time')

    # Split the time interval
    start_time, end_time = time_interval.split('-')

    # Check if any booking overlaps with the selected time range
    existing_booking = booking.objects.filter(
        doctor_id=doctor_id,
        date=date,
        start_time__lt=end_time,  # Check if start time overlaps
        end_time__gt=start_time   # Check if end time overlaps
    ).exists()

    if existing_booking:
        return JsonResponse({'error': 'This time slot is already booked for the selected doctor.'}, status=400)

    return JsonResponse({'success': 'Time slot is available.'})


#hadmin

def hadmindashboard (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])
    return render(request,"dashboard/hadmindashboard.html",{"admindetials":hload})

def hadminprofile (request): 
    hload=hadmin.objects.filter()    
    return render(request,"profile/hadminprofile.html",{"admindetials":hload})

def hadminpatientlist (request):
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    pl=patient.objects.all()
    return render(request,"list/hadminpatientlist.html",{"admindetials":hload,"patientlists":pl})

def hadmindoctorlist (request):
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    dl=doctor.objects.all()
    return render(request,"list/hadmindoctorlist.html",{"admindetials":hload,"doctorlists":dl})

def hadminmedicinelist (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    ml=medicine.objects.all()
    return render(request,"list/hadminmedicinelist.html",{"admindetials":hload,"medicinelists":ml})

def hadmindepartmentlist (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    dpl=department.objects.all()
    return render(request,"list/hadmindepartmentlist.html",{"admindetials":hload,"departmentlists":dpl})


#billingadmin

def billingadmindashboard (request): 
    bload=billingadmin.objects.filter(id=request.session["billingadmin_id"])    
    return render(request,"dashboard/billingadmindashboard.html",{"billingadmindetials":bload})

def billingadminprofile (request): 
    bload=billingadmin.objects.filter(id=request.session["billingadmin_id"])    
    return render(request,"profile/billingadminprofile.html",{"billingadmindetials":bload})

def bill(request):
    bl=pprescription.objects.all()
    pl=patient.objects.all()
    ml=medicine.objects.all()  
    bload=billingadmin.objects.filter(id=request.session["billingadmin_id"])    
    return render(request,"list/bill.html",{"billingadmindetials":bload,"prescriptionlists":pl})


#register

def patientreg (request): 
    hload=hadmin.objects.filter()    
    return render(request,"form/register/patientreg.html",{"admindetials":hload})

def patientregsave (request):
    prs=patient()
    prs.name=request.POST.get("name")
    prs.password=request.POST.get("password")
    prs.age=request.POST.get("age")
    prs.email=request.POST.get("email")
    prs.gender=request.POST.get("gender")
    prs.number=request.POST.get("number")
    prs.img=request.FILES["img"]
    prs.save()
    return patientreg(request)

def doctorreg (request): 
    hload=hadmin.objects.filter() 
    dplt=department.objects.all()   
    return render(request,"form/register/doctorreg.html",{"admindetials":hload,"departmentlists":dplt})

def doctorregsave (request):
    drs=doctor()    
    drs.name=request.POST.get("name")
    drs.password=request.POST.get("password")
    drs.age=request.POST.get("age")
    drs.email=request.POST.get("email")
    drs.gender=request.POST.get("gender")
    drs.number=request.POST.get("number")
    drs.date=request.POST.get("date")
    drs.time=request.POST.get("time")
    drs.departments=get_object_or_404(department,pk=request.POST.get("department"))

    drs.img=request.FILES["img"]
    drs.save()
    return doctorreg(request)

def billingadminreg (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    return render(request,"form/register/billingadminreg.html",{"admindetials":hload})

def billingadminregsave (request):
    bas=billingadmin()    
    bas.name=request.POST.get("name")
    bas.password=request.POST.get("password")    
    bas.email=request.POST.get("email")    
    bas.number=request.POST.get("number")    
    bas.save()
    return billingadminreg(request)

def departmentreg (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    return render(request,"form/register/departmentreg.html",{"admindetials":hload})

def departmentsave (request):
    dps=department()
    dps.name=request.POST.get("name")
    dps.bio=request.POST.get("bio")
    dps.save()
    return departmentreg(request)

def medicinereg (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    return render(request,"form/register/medicinereg.html",{"admindetials":hload})

def medicinesave (request):
    ms=medicine()
    ms.name=request.POST.get("name")
    ms.use=request.POST.get("use")
    ms.price=request.POST.get("price")
    ms.save()
    return medicinereg(request)


#delete

def delete_bookinglist(request, id):     
    item = get_object_or_404(booking, pk=id)
    item.delete()   
    return JsonResponse({'success': True})


#edit

def editb (request): 
    bload=billingadmin.objects.filter(id=request.session["billingadmin_id"])    
    return render(request,"edit/editb.html",{"billingadmindetials":bload})

def editbsave (request):
    etb=billingadmin.objects.get(pk=request.POST.get("id"))    
    etb.name=request.POST.get("name")
    etb.email=request.POST.get("email")
    etb.password=request.POST.get("password")
    etb.number=request.POST.get("number")
    etb.save()    
    return billingadmindashboard (request)

def edith (request): 
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    return render(request,"edit/edith.html",{"hadmindetials":hload})

def edithsave (request):
    eth=hadmin.objects.get(pk=request.POST.get("id"))
    eth.name=request.POST.get("name")
    eth.email=request.POST.get("email")
    eth.password=request.POST.get("password")
    eth.number=request.POST.get("number")
    eth.save()    
    return hadmindashboard(request)


def editd (request): 
    dload=doctor.objects.filter(id=request.session["doctor_id"])    
    return render(request,"edit/editd.html",{"doctordetials":dload})

def editdsave (request):
    etd=doctor.objects.get(pk=request.POST.get("id"))
    etd.name=request.POST.get("name")
    etd.email=request.POST.get("email")
    etd.password=request.POST.get("password")
    etd.age=request.POST.get("age")
    etd.number=request.POST.get("number")
    etd.gender=request.POST.get("gender")
    etd.img=request.FILES["img"]
    etd.save()    
    return doctordashboard(request)

def editp (request): 
    pload=patient.objects.filter(id=request.session["patient_id"])    
    return render(request,"edit/editp.html",{"patientdetials":pload})

def editpsave (request):
    etp=patient.objects.get(pk=request.POST.get("id"))
    etp.name=request.POST.get("name")
    etp.email=request.POST.get("email")
    etp.password=request.POST.get("password")
    etp.age=request.POST.get("age")
    etp.number=request.POST.get("number")
    etp.gender=request.POST.get("gender")
    etp.img=request.FILES["img"]
    etp.save()    
    return patientdashboard(request)



#logout

def hadminlogout (request):
    if 'hadmin_id' in request.session:
        request.session["hadmin_id"] = 0
        del request.session['hadmin_id']        
    logout(request)
    return redirect(home)

def doctorlogout (request):
    if 'doctor_id' in request.session:
        request.session["doctor_id"] = 0
        del request.session['doctor_id']        
    logout(request)
    return redirect(home)

def patientlogout (request):
    if 'patient_id' in request.session:
        request.session["patient_id"] = 0
        del request.session['patient_id']        
    logout(request)
    return redirect(home)

def billingadminlogout (request):
    if 'billingadmin_id' in request.session:
        request.session["billingadmin_id"] = 0
        del request.session['billingadmin_id']
    logout(request)
    return redirect(home)


#java

def fetch_medicine(request, patientId):
    #med = medicine.objects.filter(pprescription__patientname=patientId).values('id', 'name', 'use', 'price')
    med = pprescription.objects.filter(patientname__id=patientId).values('id','medicinename_id__name','medicinename_id__use','medicinename_id__price','quantity')  
    return JsonResponse(list(med), safe=False)

def fetch_doctor(request, doctorId):    
    dd = doctor.objects.filter(id=doctorId).values('id', 'name', 'time', 'date')  
    return JsonResponse(list(dd), safe=False)



# Fetch patients registered in the selected month
def fetch_patients(request):
    # Get the selected month and year from the request
    month_year = request.GET.get('month')  # e.g., "2023-09"
    
    if month_year:
        try:
            # Split the value into year and month
            year, month = month_year.split('-')

            # Filter patients based on the year and month of the reg_date field
            patients = patient.objects.filter(reg_date__year=year, reg_date__month=month)

            # Convert the queryset to a list of dictionaries
            patient_data = [
                {
                    'id': patient.id,
                    'name': patient.name,
                    'reg_date': patient.reg_date.strftime('%Y-%m-%d %H:%M:%S')
                }
                for patient in patients
            ]

            # Return the data as JSON
            return JsonResponse(patient_data, safe=False)

        except ValueError:
            return JsonResponse({'error': 'Invalid month format'}, status=400)
    
    return JsonResponse({'error': 'Invalid month selected'}, status=400)


# Fetch purchases and revenue report for the selected month
def fetch_purchases(request):
    month_year = request.GET.get('month', None)
    
    if month_year:
        try:
            # Split the value into year and month
            year, month = month_year.split('-')

            # Calculate the start and end dates for the selected month
            start_date = datetime(int(year), int(month), 1)
            if int(month) == 12:
                end_date = datetime(int(year) + 1, 1, 1)
            else:
                end_date = datetime(int(year), int(month) + 1, 1)

            # Use lowercase `purchase` for the model name, as per your model
            purchases = purchase.objects.filter(purchase_date__gte=start_date, purchase_date__lt=end_date)

            purchase_list = []            
            total_revenue = 0.0
            # Change the variable name from `purchase` to avoid conflict with the model name
            for p in purchases:
                
                
                price = float(p.medicine.price)
                quantity = int(p.quantity)

                total_cost = price * quantity
                int(total_cost)
                
                total_revenue = total_cost + total_revenue

                purchase_list.append({
                    'patient_name': p.patient.name,  # Assuming you have a `patients` ForeignKey in `purchase`
                    'medicine_name': p.medicine.name,  # Assuming `medicines` ForeignKey in `purchase`
                    'quantity': p.quantity,
                    'total_cost': total_cost,
                    'purchase_date': p.purchase_date.strftime('%Y-%m-%d'),
                })

            # Return purchase data and total revenue
            return JsonResponse({
                'purchases': purchase_list,
                'total_revenue': total_revenue
            })
        
        except ValueError:
            return JsonResponse({'error': 'Invalid month format'}, status=400)
    
    return JsonResponse({'error': 'Month not provided'}, status=400)




def save_purchase(request, patient_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        patient_instance = patient.objects.get(id=patient_id)  # Corrected variable name
        
        for item in data:
            mn = item['medicine_name']
            quantity = item['quantity']
            
            # Use filter to get all medicines with the given name
            medicine_instances = medicine.objects.filter(name=mn)
            
            if not medicine_instances.exists():
                return JsonResponse({'success': False, 'error': f'Medicine {mn} not found'}, status=404)
            
            # Assuming you want to create a purchase for each matching medicine
            for medicine_instance in medicine_instances:
                purchase.objects.create(
                    patient=patient_instance, 
                    medicine=medicine_instance, 
                    quantity=quantity
                )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False}, status=400)






#report

def reportview (request):
    hload=hadmin.objects.filter(id=request.session["hadmin_id"])    
    return render(request,"report/reportviewcopy.html",{"admindetials":hload})