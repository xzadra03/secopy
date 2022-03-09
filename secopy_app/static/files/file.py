import tempfile

file = tempfile.TemporaryFile()
file.write(b"This is temporary file")
file.seek(0)
print(file.read())
file.close()


