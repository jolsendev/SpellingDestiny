import pysftp as sftp

def push_file_to_server(file):
	cnopts = sftp.CnOpts()
	cnopts.hostkeys = None
	s = sftp.Connection(
		host="138.68.19.177", 
		username="root", 
		password="",
		cnopts=cnopts)
	local_path = "./Words/"+file
	remote_path = "/home/Words/"+file

	s.put(local_path, remote_path)
	s.close()

def get_file_to_server(file):
	cnopts = sftp.CnOpts()
	cnopts.hostkeys = None
	s = sftp.Connection(
		host="138.68.19.177", 
		username="root", 
		password="",
		cnopts=cnopts)
	local_path = "./Words/"+file
	remote_path = "/home/Words/"+file

	s.get(remote_path, local_path)
	s.close()

#push_file_to_server("3rd_grade.txt");
#push_file_to_server("4th_grade.txt");
#push_file_to_server("5th_grade.txt");
#push_file_to_server("6th_grade.txt");

#get_file_to_server("3rd_grade.txt");
#get_file_to_server("4th_grade.txt");
#get_file_to_server("5th_grade.txt");
#get_file_to_server("6th_grade.txt");