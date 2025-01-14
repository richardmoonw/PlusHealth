from DatabaseConnection import connection
import hashlib

class DoctorDAO:
	#Creates the doctor in the database when you first sign up
	#Before add_doctor
	def create_new_doctor(doctor):
		conn = connection.Connection.make_connection()

		cur = conn.cursor()

		encrypted_pwd = hashlib.sha256(doctor.password.encode()).hexdigest()

		cur.execute("SELECT id FROM Hospital WHERE name='" + doctor.hospital + "'") 
		hospital_id = cur.fetchone()

		cur.execute("SELECT id FROM School WHERE name='" + doctor.school + "'") 
		school_id = cur.fetchone()

		cur.execute("INSERT INTO Doctor (first_name, last_name, birthdate, sex, phone_number, medical_degree, \
					speciality, email, password, hospital_id, school_id, graduation_date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", \
					(doctor.first_name, doctor.last_name, doctor.birthdate, doctor.sex, doctor.phone, None, \
					doctor.speciality, doctor.email, encrypted_pwd, hospital_id[0], school_id[0], doctor.graduation_date))

		conn.commit()

		cur.execute('SELECT MAX(id) FROM Doctor')
		doctor = cur.fetchone()

		conn.close()

		return doctor

	#get the password of a specified doctor
	def validate_login(email):
		conn = connection.Connection.make_connection()

		cur = conn.cursor()

		cur.execute("SELECT id, password FROM Doctor WHERE email ='" + email + "'")
		user = cur.fetchone()

		return user

	#Get all the atributes of the doctor
	def get_doctor(id):
		conn = connection.Connection.make_connection()

		cur = conn.cursor()

		cur.execute("SELECT * FROM Doctor JOIN Hospital ON Doctor.hospital_id=Hospital.id \
					JOIN School ON Doctor.school_id=School.id WHERE Doctor.id=" + str(id))

		doctor = cur.fetchone()

		return doctor

	#Adds degree to the database
	def create_degree(doctor):
		conn = connection.Connection.make_connection()

		cur = conn.cursor()
		print(doctor.filename)
		print(doctor._id)
		cur.execute("UPDATE Doctor SET medical_degree='" + doctor.filename + "' WHERE id = " + str(doctor._id))
		conn.commit()

		conn.close()