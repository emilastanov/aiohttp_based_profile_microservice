run:
	docker run -d -p 8080:8080 --rm --name ast_profile-container apaem/astpro-profile
pull:
	git pull
	docker stop ast_profile-container
	docker build . --tag apaem/astpro-profile
	docker run -d -p 8081:8080 --rm --name ast_profile-container apaem/astpro-profile
stop:
	docker stop ast_profile-container
reload:
	make stop
	make run

