prepare:
	rm -f sodalite && rm -f radon && \
	ln -sf ../iac-modules sodalite && \
	ln -sf ../localToS3Pipeline radon

deploy: prepare
	opera deploy -i input.yaml service.yaml

deploy-test: prepare
	opera deploy -i input.yaml test_service.yaml

clean:
	rm -rf .opera

clean-all:
	rm -rf .opera && sed -i 's/:.*/:/' input.yaml