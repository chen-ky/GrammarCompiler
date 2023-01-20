CONTAINER_BUILDER=podman
JIT_CONTAINER_TAG=bf
NO_JIT_CONTAINER_TAG=bf-nojit


jit: Dockerfile main.py
	$(CONTAINER_BUILDER) build -f Dockerfile -t $(JIT_CONTAINER_TAG) ./

no-jit: Dockerfile_nojit main.py
	$(CONTAINER_BUILDER) build -f Dockerfile_nojit -t $(NO_JIT_CONTAINER_TAG) ./
