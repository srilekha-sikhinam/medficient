# import openpyxl and tkinter modules
import sys
import platform
plat = platform.system()
if plat == 'Windows':
    sys.path.insert(0, 'src\helpers')
    sys.path.insert(0, 'src\models')
elif plat =='Linux' or plat=='Darwin':
    sys.path.insert(0, 'src/helpers')
    sys.path.insert(0, 'src/models')

from tkinter import *
from tkinter import ttk
from predict_model import *


# Function to set focus (cursor)
def focus1(event):
	# set focus on the course_field box
	hospital_service_area_entry.focus_set()


# Function to set focus
def focus2(event):
	# set focus on the sem_field box
	hospital_county_entry.focus_set()


# Function to set focus
def focus3(event):
	# set focus on the form_no_field box
	perm_facility_entry.focus_set()


# Function to set focus
def focus4(event):
	# set focus on the contact_no_field box
	clicked_age_group.focus_set()


# Function to set focus
def focus5(event):
	# set focus on the email_id_field box
	clicked_gender.focus_set()


# Function to set focus
def focus6(event):
	# set focus on the address_field box
	clicked_race.focus_set()

def focus7(event):
	clicked_ethnicity.focus_set()

def focus8(event):
	clicked_type_of_admission.focus_set()

def focus9(event):
	clicked_ccsr_diagnosis_code.focus_set()

def focus10(event):
	clicked_ccsr_procedure_code.focus_set()

def focus11(event):
	clicked_apr_drg_code.focus_set()

def focus12(event):
	clicked_apr_mdc_code.focus_set()

def focus13(event):
	clicked_apr_severity_of_illness_code.focus_set()

def focus14(event):
	clicked_apr_risk_of_mortality.focus_set()

def focus15(event):
	clicked_apr_med_surg_desc.focus_set()

def focus16(event):
	clicked_payment_typology.focus_set()

def focus17(event):
	clicked_er_indicator.focus_set()


# Function for clearing the
# contents of text entry boxes
def clear():
	
	# clear the content of text entry box
	clicked_age_group.set( "0 to 17" )
	clicked_gender.set( "Male" )
	clicked_race.set( "White" )
	clicked_ethnicity.set( "Not Span/Hispanic" )
	clicked_type_of_admission.set( "Elective" )
	clicked_ccsr_diagnosis_code.set( 659 )
	clicked_ccsr_procedure_code.set( 0 )
	clicked_apr_drg_code.set( 194.0 )
	clicked_apr_mdc_code.set( 19. )
	clicked_apr_severity_of_illness_code.set( 1 )
	clicked_apr_risk_of_mortality.set( "Minor" )
	clicked_apr_med_surg_desc.set( "Medical" )
	clicked_payment_typology.set( "Medicare" )
	clicked_er_indicator.set( "No" )


# Function to take data from GUI
# window and write to an excel file
def insert():
	hospital_service_area = hospital_service_area_entry.get()
	hospital_county = hospital_county_entry.get()
	perm_facility_id = perm_facility_entry.get()
	age_group = clicked_age_group.get()
	gender = clicked_gender.get()
	race = clicked_race.get()
	ethnicity = clicked_ethnicity.get()
	type_of_admission = clicked_type_of_admission.get()
	ccsr_diagnosis_code = clicked_ccsr_diagnosis_code.get()
	ccsr_procedure_code = clicked_ccsr_procedure_code.get()
	apr_drg_code = clicked_apr_drg_code.get()
	apr_mdc_code = clicked_apr_mdc_code.get()
	apr_severity_of_illness_code = clicked_apr_severity_of_illness_code.get()
	apr_risk_of_mortality = clicked_apr_risk_of_mortality.get()
	apr_med_surg_desc = clicked_apr_med_surg_desc.get()
	payment_typology = clicked_payment_typology.get()
	er_indicator = clicked_er_indicator.get()

	feature_arr = {
		'Hospital Service Area': hospital_service_area, 
		'Hospital County': hospital_county, 
		'Permanent Facility Id': perm_facility_id,
		'Age Group': age_group, 
		'Gender': gender,
		'Race': race, 
		'Ethnicity': ethnicity,
		'Type of Admission': type_of_admission,
		'CCSR Diagnosis Code': ccsr_diagnosis_code, 
		'CCSR Procedure Code': ccsr_procedure_code,
		'APR DRG Code': apr_drg_code,
		'APR MDC Code': apr_mdc_code, 
		'APR Severity of Illness Code': apr_severity_of_illness_code,
		'APR Risk of Mortality': apr_risk_of_mortality,
		'APR Medical Surgical Description': apr_med_surg_desc,
		'Payment Typology 1': payment_typology,
		'Emergency Department Indicator': er_indicator
	}

	options_arr = {
		'Hospital Service Area': ['New York City', 'Hudson Valley', 'Finger Lakes', 'Capital/Adirond',
 'Long Island', 'Central NY', 'Western NY', 'Southern Tier'], 
		'Hospital County': ['Manhattan', 'Westchester', 'Bronx', 'Kings', 'Livingston', 'Orange'
, 'Rockland', 'Columbia', 'Nassau', 'Queens', 'Madison', 'Onondaga', 'Sullivan'
, 'Suffolk', 'Allegany', 'Erie', 'Rensselaer', 'Richmond', 'Niagara', 'Jefferson'
, 'Oneida', 'Otsego', 'Schenectady', 'Monroe', 'Ontario', 'Steuben', 'Albany'
, 'Franklin', 'Ulster', 'Genesee', 'Wyoming', 'Chemung', 'Wayne', 'Broome'
, 'Chenango', 'Fulton', 'Montgomery', 'Dutchess', 'Putnam', 'Cattaraugus'
, 'Cayuga', 'Cortland', 'Oswego', 'St Lawrence', 'Tompkins', 'Saratoga', 'Lewis'
, 'Clinton', 'Chautauqua', 'Warren'], 
		'Permanent Facility Id': perm_facility_id,
		'Age Group': age_group_options, 
		'Gender': gender_options,
		'Race': race_options, 
		'Ethnicity': ethnicity_options,
		'Type of Admission': type_of_admission_options,
		'CCSR Diagnosis Code': ccsr_diagnosis_code_options, 
		'CCSR Procedure Code': ccsr_procedure_code_options,
		'APR DRG Code': apr_drg_codes_options,
		'APR MDC Code': apr_mdc_code_options, 
		'APR Severity of Illness Code': [1, 2, 3, 4],
		'APR Medical Surgical Description': apr_med_surg_desc_options,
		'Payment Typology 1': payment_typology_options,
		'Emergency Department Indicator': er_indicator_options
	}

	predicted_days = get_prediction(feature_arr, options_arr)

	hospital_service_area_entry.focus_set()

	clear()
	clicked_age_group_drop.config(state= "disabled")
	clicked_gender_drop.config(state= "disabled")
	clicked_race_drop.config(state= "disabled")
	clicked_ethnicity_drop.config(state= "disabled")
	clicked_type_of_admission_drop.config(state="disabled")
	clicked_ccsr_diagnosis_code_drop.config(state="disabled")
	clicked_ccsr_procedure_code_drop.config(state="disabled")
	clicked_apr_drg_code_drop.config(state="disabled")
	clicked_apr_mdc_code_drop.config(state="disabled")
	clicked_apr_severity_of_illness_code_drop.config(state="disabled")
	clicked_apr_risk_of_mortality_drop.config(state="disabled")
	clicked_apr_drg_code_drop.config(state="disabled")
	clicked_apr_med_surg_desc_drop.config(state="disabled")
	clicked_payment_typology_drop.config(state="disabled")
	clicked_er_indicator_drop.config(state="disabled")
	submit.config(state="disabled")

	#Set the geometry of Tkinter frame

	top= Toplevel(root)
	top.geometry("500x250")
	top.title("Predictions")
	Label(top, text= "Predictions:\nLength of Stay: " + predicted_days[0][0].replace('to', '-') + " days\n" + "Total Cost: $" + predicted_days[1][0].replace(' - ', ' - $'), font=("Arial", 12)).place(x=150,y=80)
	x = root.winfo_x()
	y = root.winfo_y()
	top.geometry("+%d+%d" %(x+200,y+200))


# Driver code
if __name__ == "__main__":
	
	# create a GUI window
	root = Tk()

	# set the background colour of GUI window
	root.configure(background='#BFBFEF')

	# set the title of GUI window
	root.title("Patient Information Form")

	# set the configuration of GUI window
	root.geometry("1100x600")

	# create a Name label
	hospital_service_area_label = Label(root, text="Hospital Service Area", bg="#BFBFEF")

	# create a Course label
	hospital_county_label = Label(root, text="Hospital County", bg="#BFBFEF")

	# create a Semester label
	perm_facility_id_label = Label(root, text="Permanent Facility ID", bg="#BFBFEF")

	# create a Form No. label
	age_group_label = Label(root, text="Age Group", bg="#BFBFEF")

	# create a Contact No. label
	gender_label = Label(root, text="Gender", bg="#BFBFEF")

	# create a Email id label
	race_label = Label(root, text="Race", bg="#BFBFEF")

	# create a address label
	ethnicity_label = Label(root, text="Ethnicity", bg="#BFBFEF")

	admission_type_label = Label(root, text="Type of Admission", bg="#BFBFEF")

	ccsr_diagnosis_code_label = Label(root, text="CCSR Diagnosis Code", bg="#BFBFEF")

	ccsr_procedure_code_label = Label(root, text="CCSR Procedure Code", bg="#BFBFEF")

	apr_drg_code_label = Label(root, text="APR DRG Code", bg="#BFBFEF")

	apr_mdc_label = Label(root, text="APR MDC Code", bg="#BFBFEF")

	apr_severity_of_illness_code_label = Label(root, text="APR Severity of Illness Code", bg="#BFBFEF")

	apr_risk_of_mortality_label = Label(root, text="APR Risk of Mortality", bg="#BFBFEF")

	apr_med_surg_description_label = Label(root, text="APR Medical Surgical Desciption", bg="#BFBFEF")

	payment_typology_1_label = Label(root, text="Payment Typology", bg="#BFBFEF")

	emergency_department_indicator_label = Label(root, text="Emergency Department Indicator", bg="#BFBFEF")

	hospital_service_area_options = ['Hudson Valley', 'New York City', 'Western NY', 'Central NY', 'Capital/Adirond', 'Finger Lakes', 'Long Island', 'Southern Tier']

	hospital_county_options = ['Westchester', 'Manhattan', 'Sullivan', 'Erie', 'Kings', 'Onondaga', 'Schenectady', 'Bronx', 'Livingston', 'Orange', 'Rockland', 'Otsego', 'Columbia', 'Delaware', 'Niagara', 'Rensselaer', 'Richmond', 'Nassau', 'Suffolk', 'Queens', 'Steuben', 'Jefferson', 'Madison', 'Allegany', 'Chemung', 'Herkimer', 'Albany', 'Essex', 'Schoharie', 'Ontario', 'Oneida', 'St Lawrence', 'Ulster', 'Monroe', 'Clinton', 'Franklin', 'Chautauqua', 'Schuyler', 'Montgomery', 'Genesee', 'Wyoming', 'Orleans', 'Wayne', 'Yates', 'Oswego', 'Broome', 'Chenango', 'Lewis', 'Fulton', 'Dutchess', 'Putnam', 'Cattaraugus', 'Cayuga', 'Cortland', 'Tompkins', 'Saratoga', 'Warren']

	age_group_options = ['0 to 17', '18 to 29', '30 to 49', '50 to 69',  '70 or Older']

	gender_options = ['Male', 'Female', 'Unknown']

	race_options = ['White', 'Black/African American', 'Other Race', 'Multi-racial']

	ethnicity_options = ['Not Span/Hispanic', 'Spanish/Hispanic', 'Unknown', 'Multi-ethnic']

	type_of_admission_options = ['Elective', 'Emergency', 'Newborn', 'Urgent', 'Trauma', 'Not Available']

	ccsr_diagnosis_code_options = [659, 99, 108, 159, 127, 203, 237, 209, 130, 133, 198, 225, 9, 42, 224, 54, 212, 202, 238, 204, 163, 230, 21, 1, 8, 226, 231, 207, 217, 211, 161, 236, 44, 201, 232, 244, 132]

	ccsr_procedure_code_options = [0, 108, 193, 216, 183, 177, 231, 218, 41, 152, 58, 210, 227, 174, 19, 213, 147, 222, 197, 54, 70, 178, 204, 226, 39, 88, 93, 162, 203, 202, 29, 180, 179, 92, 215, 65, 37, 71, 47, 225, 4, 102, 83, 219, 91, 31, 49, 217, 192, 199, 155, 173, 201, 228, 100, 76, 223, 194, 32, 61, 156, 63, 187, 208, 191, 198, 101, 95, 224, 111, 195, 171, 130, 98, 110, 34, 62, 221, 142, 175, 229, 97, 69, 40, 214, 27, 107, 159, 212, 196, 8, 185, 211, 148, 77, 26, 145, 48, 205, 35, 163, 207, 181, 189, 170, 11, 73, 200, 25, 165, 146, 190, 164, 5, 131, 12, 109, 139, 168, 117, 160, 116, 161, 74, 188, 220, 115, 172, 50, 82, 150, 1, 67, 42, 158]

	apr_drg_codes_options = [194.0, 140.0, 750.0, 463.0, 302.0]

	apr_mdc_code_options = [19.,  5., 11.,  4.,  8.]

	apr_severity_of_illness_code_options = ['Minor', 'Moderate', 'Major', 'Extreme']

	apr_risk_of_mortality_options = ['Minor', 'Moderate', 'Major', 'Extreme']

	apr_med_surg_desc_options = ['Surgical']

	payment_typology_options = ['Private Health Insurance', 'Medicare', 'Blue Cross/Blue Shield', 'Medicaid',
 'Miscellaneous/Other', 'Self-Pay', 'Managed Care, Unspecified',
 'Federal/State/Local/VA', 'Department of Corrections', 'Unknown']

	er_indicator_options = ['Yes', 'No']

	hospital_service_area_label.grid(row=1, column=0, padx=20, pady=20,sticky="ew")
	hospital_county_label.grid(row=2, column=0, sticky="ew")
	perm_facility_id_label.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
	age_group_label.grid(row=4, column=0, sticky="ew")
	gender_label.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
	race_label.grid(row=6, column=0, sticky="ew")
	ethnicity_label.grid(row=7, column=0, padx=20, pady=20, sticky="ew")
	admission_type_label.grid(row=8, column=0, sticky="ew")
	ccsr_diagnosis_code_label.grid(row=9, column=0, padx=20, pady=20, sticky="ew")
	ccsr_procedure_code_label.grid(row=1, column=2, sticky="ew")
	apr_drg_code_label.grid(row=2, column=2, padx=20, pady=20, sticky="ew")
	apr_mdc_label.grid(row=3, column=2, sticky="ew")
	apr_severity_of_illness_code_label.grid(row=4, column=2, padx=20, pady=20, sticky="ew")
	apr_risk_of_mortality_label.grid(row=5, column=2, sticky="ew")
	apr_med_surg_description_label.grid(row=6, column=2, padx=20, pady=20, sticky="ew")
	payment_typology_1_label.grid(row=7, column=2, sticky="ew")
	emergency_department_indicator_label.grid(row=8, column=2, padx=20, pady=20, sticky="ew")

	hospital_service_area_entry = Entry(root)
	#hospital_service_area_entry.pack()
	hospital_service_area_entry.insert(0, "New York City")
	hospital_service_area_entry.config(state= "disabled")

	hospital_county_entry = Entry(root)
	#hospital_county_entry.pack()
	hospital_county_entry.insert(0, "Manhattan")
	hospital_county_entry.config(state= "disabled")

	perm_facility_entry = Entry(root)
	#perm_facility_entry.pack()
	perm_facility_entry.insert(0, 1456.0)
	perm_facility_entry.config(state= "disabled")

	clicked_age_group = StringVar()
	clicked_age_group.set( "0 to 17" )
	clicked_age_group_drop = OptionMenu( root , clicked_age_group , *age_group_options)
	#clicked_age_group_drop.pack()

	clicked_gender = StringVar()
	clicked_gender.set( "Male" )
	clicked_gender_drop = OptionMenu( root , clicked_gender , *gender_options)
	#clicked_gender_drop.pack()

	clicked_race = StringVar()
	clicked_race.set( "White" )
	clicked_race_drop = OptionMenu( root , clicked_race , *race_options)
	#clicked_race_drop.pack()

	clicked_ethnicity = StringVar()
	clicked_ethnicity.set( "Not Span/Hispanic" )
	clicked_ethnicity_drop = OptionMenu( root , clicked_ethnicity , *ethnicity_options)
	#clicked_ethnicity_drop.pack()

	clicked_type_of_admission = StringVar()
	clicked_type_of_admission.set( "Elective" )
	clicked_type_of_admission_drop = OptionMenu( root , clicked_type_of_admission , *type_of_admission_options)
	#clicked_type_of_admission_drop.pack()

	clicked_ccsr_diagnosis_code = IntVar()
	clicked_ccsr_diagnosis_code.set( 659 )
	clicked_ccsr_diagnosis_code_drop = OptionMenu( root , clicked_ccsr_diagnosis_code , *ccsr_diagnosis_code_options)
	#clicked_ccsr_diagnosis_code_drop.pack()

	clicked_ccsr_procedure_code = IntVar()
	clicked_ccsr_procedure_code.set( 0 )
	clicked_ccsr_procedure_code_drop = OptionMenu( root , clicked_ccsr_procedure_code , *ccsr_procedure_code_options)
	#clicked_ccsr_procedure_code_drop.pack()

	clicked_apr_drg_code = DoubleVar()
	clicked_apr_drg_code.set( 194.0 )
	clicked_apr_drg_code_drop = OptionMenu( root , clicked_apr_drg_code , *apr_drg_codes_options)
	#clicked_apr_drg_code_drop.pack()

	clicked_apr_mdc_code = DoubleVar()
	clicked_apr_mdc_code.set( 19. )
	clicked_apr_mdc_code_drop = OptionMenu( root , clicked_apr_mdc_code , *apr_mdc_code_options)
	#clicked_apr_mdc_code_drop.pack()

	clicked_apr_severity_of_illness_code = StringVar()
	clicked_apr_severity_of_illness_code.set( "Minor" )
	clicked_apr_severity_of_illness_code_drop = OptionMenu( root , clicked_apr_severity_of_illness_code , *apr_severity_of_illness_code_options)
	#clicked_apr_severity_of_illness_code_drop.pack()

	clicked_apr_risk_of_mortality = StringVar()
	clicked_apr_risk_of_mortality.set( "Minor" )
	clicked_apr_risk_of_mortality_drop = OptionMenu( root , clicked_apr_risk_of_mortality , *apr_risk_of_mortality_options)
	#clicked_apr_risk_of_mortality_drop.pack()

	clicked_apr_med_surg_desc = StringVar()
	clicked_apr_med_surg_desc.set( "Surgical" )
	clicked_apr_med_surg_desc_drop = OptionMenu( root , clicked_apr_med_surg_desc , *apr_med_surg_desc_options)
	#clicked_apr_med_surg_desc_drop.pack()

	clicked_payment_typology = StringVar()
	clicked_payment_typology.set( "Medicare" )
	clicked_payment_typology_drop = OptionMenu( root , clicked_payment_typology , *payment_typology_options)
	#clicked_payment_typology_drop.pack()

	clicked_er_indicator = StringVar()
	clicked_er_indicator.set( "No" )
	clicked_er_indicator_drop = OptionMenu( root , clicked_er_indicator , *er_indicator_options)
	#clicked_er_indicator_drop.pack()

	hospital_service_area_entry.bind("<Return>", focus1)
	hospital_county_entry.bind("<Return>", focus2)
	perm_facility_entry.bind("<Return>", focus3)
	clicked_age_group_drop.bind("<Return>", focus4)
	clicked_gender_drop.bind("<Return>", focus5)
	clicked_race_drop.bind("<Return>", focus6)
	clicked_ethnicity_drop.bind("<Return>", focus7)
	clicked_type_of_admission_drop.bind("<Return>", focus8)
	clicked_ccsr_diagnosis_code_drop.bind("<Return>", focus9)
	clicked_ccsr_procedure_code_drop.bind("<Return>", focus10)
	clicked_apr_drg_code_drop.bind("<Return>", focus11)
	clicked_apr_mdc_code_drop.bind("<Return>", focus12)
	clicked_apr_severity_of_illness_code_drop.bind("<Return>", focus13)
	clicked_apr_risk_of_mortality_drop.bind("<Return>", focus14)
	clicked_apr_med_surg_desc_drop.bind("<Return>", focus15)
	clicked_payment_typology_drop.bind("<Return>", focus16)
	clicked_er_indicator_drop.bind("<Return>", focus17)

	hospital_service_area_entry.grid(row=1, column=1, ipadx="100", sticky="ew")
	hospital_county_entry.grid(row=2, column=1, ipadx="100", sticky="ew")
	perm_facility_entry.grid(row=3, column=1, ipadx="100", sticky="ew")
	clicked_age_group_drop.grid(row=4, column=1, ipadx="100", sticky="ew")
	clicked_gender_drop.grid(row=5, column=1, ipadx="100", sticky="ew")
	clicked_race_drop.grid(row=6, column=1, ipadx="100", sticky="ew")
	clicked_ethnicity_drop.grid(row=7, column=1, ipadx="100", sticky="ew")
	clicked_type_of_admission_drop.grid(row=8, column=1, ipadx="100", sticky="ew")
	clicked_ccsr_diagnosis_code_drop.grid(row=9, column=1, ipadx="100", sticky="ew")
	clicked_ccsr_procedure_code_drop.grid(row=1, column=3, ipadx="100", sticky="ew")
	clicked_apr_drg_code_drop.grid(row=2, column=3, ipadx="100", sticky="ew")
	clicked_apr_mdc_code_drop.grid(row=3, column=3, ipadx="100", sticky="ew")
	clicked_apr_severity_of_illness_code_drop.grid(row=4, column=3, ipadx="100", sticky="ew")
	clicked_apr_risk_of_mortality_drop.grid(row=5, column=3, ipadx="100", sticky="ew")
	clicked_apr_med_surg_desc_drop.grid(row=6, column=3, ipadx="100", sticky="ew")
	clicked_payment_typology_drop.grid(row=7, column=3, ipadx="100", sticky="ew")
	clicked_er_indicator_drop.grid(row=8, column=3, ipadx="100", sticky="ew")


	# create a Submit Button and place into the root window
	submit = Button(root, text="Submit", fg="Black",
							bg="#686883", command=insert)
	submit.grid(row=9, column=3, sticky='ew')

	# start the GUI
	root.mainloop()
