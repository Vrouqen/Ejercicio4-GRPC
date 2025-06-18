from concurrent import futures
import grpc
import grades_pb2
import grades_pb2_grpc
from services.student_services import calculate_average

class GradeServiceServicer(grades_pb2_grpc.GradeServiceServicer):
    def GetGradesAverage(self, request, context):
        avg = calculate_average()
        return grades_pb2.GradeAverageResponse(average=avg)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grades_pb2_grpc.add_GradeServiceServicer_to_server(GradeServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
