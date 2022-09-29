## Build
FROM golang:1.16-buster AS build

WORKDIR /app

COPY go.mod ./  

COPY *.go ./

RUN go build -o /client

## Deploy
FROM gcr.io/distroless/base-debian10

WORKDIR /

COPY --from=build /client /client

USER nonroot:nonroot

ENTRYPOINT ["/client"]