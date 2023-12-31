# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventory_pb2 as inventory__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchByID = channel.unary_stream(
                '/inventory.InventoryService/SearchByID',
                request_serializer=inventory__pb2.SearchByIDRequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecord.FromString,
                )
        self.SearchBySKU = channel.unary_stream(
                '/inventory.InventoryService/SearchBySKU',
                request_serializer=inventory__pb2.SearchBySKURequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecordList.FromString,
                )
        self.SearchBySKURange = channel.unary_stream(
                '/inventory.InventoryService/SearchBySKURange',
                request_serializer=inventory__pb2.SearchBySKURangeRequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRangeList.FromString,
                )
        self.GetDistribution = channel.unary_stream(
                '/inventory.InventoryService/GetDistribution',
                request_serializer=inventory__pb2.GetDistributionRequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecordList.FromString,
                )
        self.UpdateCost = channel.unary_stream(
                '/inventory.InventoryService/UpdateCost',
                request_serializer=inventory__pb2.UpdateCostRequest.SerializeToString,
                response_deserializer=inventory__pb2.UpdateResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchBySKU(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchBySKURange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDistribution(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchByID': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchByID,
                    request_deserializer=inventory__pb2.SearchByIDRequest.FromString,
                    response_serializer=inventory__pb2.InventoryRecord.SerializeToString,
            ),
            'SearchBySKU': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchBySKU,
                    request_deserializer=inventory__pb2.SearchBySKURequest.FromString,
                    response_serializer=inventory__pb2.InventoryRecordList.SerializeToString,
            ),
            'SearchBySKURange': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchBySKURange,
                    request_deserializer=inventory__pb2.SearchBySKURangeRequest.FromString,
                    response_serializer=inventory__pb2.InventoryRangeList.SerializeToString,
            ),
            'GetDistribution': grpc.unary_stream_rpc_method_handler(
                    servicer.GetDistribution,
                    request_deserializer=inventory__pb2.GetDistributionRequest.FromString,
                    response_serializer=inventory__pb2.InventoryRecordList.SerializeToString,
            ),
            'UpdateCost': grpc.unary_stream_rpc_method_handler(
                    servicer.UpdateCost,
                    request_deserializer=inventory__pb2.UpdateCostRequest.FromString,
                    response_serializer=inventory__pb2.UpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'inventory.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inventory.InventoryService/SearchByID',
            inventory__pb2.SearchByIDRequest.SerializeToString,
            inventory__pb2.InventoryRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchBySKU(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inventory.InventoryService/SearchBySKU',
            inventory__pb2.SearchBySKURequest.SerializeToString,
            inventory__pb2.InventoryRecordList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchBySKURange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inventory.InventoryService/SearchBySKURange',
            inventory__pb2.SearchBySKURangeRequest.SerializeToString,
            inventory__pb2.InventoryRangeList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDistribution(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inventory.InventoryService/GetDistribution',
            inventory__pb2.GetDistributionRequest.SerializeToString,
            inventory__pb2.InventoryRecordList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/inventory.InventoryService/UpdateCost',
            inventory__pb2.UpdateCostRequest.SerializeToString,
            inventory__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
