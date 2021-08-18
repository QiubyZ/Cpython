import  pyximport
pyximport.install()
from test import Testing

def main():
	data = Testing("QiubyZhukhi")
	print(data.getname())
	
if __name__ == "__main__":
	main()