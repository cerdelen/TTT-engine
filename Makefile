



all:
	git add *
	@read -p "Enter Module Name:" module; \
	git commit -m "$$module"

talk:
	@clear

	echo $(USERNAME)
	echo $(message)