import grpc
import grades_pb2
import grades_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grades_pb2_grpc.GradeServiceStub(channel)
        response = stub.GetGradesAverage(grades_pb2.Empty())
        print(f"Grades average: {response.average}")

if __name__ == '__main__':
    run()
