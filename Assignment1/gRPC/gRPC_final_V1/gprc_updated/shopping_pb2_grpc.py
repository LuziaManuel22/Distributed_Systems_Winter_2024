# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import shopping_pb2 as shopping__pb2


class MarketStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterSeller = channel.unary_unary(
                '/shopping.Market/RegisterSeller',
                request_serializer=shopping__pb2.SellerInfo.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.SellItem = channel.unary_unary(
                '/shopping.Market/SellItem',
                request_serializer=shopping__pb2.ItemInfo.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/shopping.Market/UpdateItem',
                request_serializer=shopping__pb2.ItemInfo.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/shopping.Market/DeleteItem',
                request_serializer=shopping__pb2.ItemID.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.DisplaySellerItems = channel.unary_unary(
                '/shopping.Market/DisplaySellerItems',
                request_serializer=shopping__pb2.SellerInfo.SerializeToString,
                response_deserializer=shopping__pb2.ItemList.FromString,
                )
        self.SearchItem = channel.unary_unary(
                '/shopping.Market/SearchItem',
                request_serializer=shopping__pb2.SearchRequest.SerializeToString,
                response_deserializer=shopping__pb2.ItemList.FromString,
                )
        self.BuyItem = channel.unary_unary(
                '/shopping.Market/BuyItem',
                request_serializer=shopping__pb2.BuyRequest.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.AddToWishList = channel.unary_unary(
                '/shopping.Market/AddToWishList',
                request_serializer=shopping__pb2.WishListRequest.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.RateItem = channel.unary_unary(
                '/shopping.Market/RateItem',
                request_serializer=shopping__pb2.RatingRequest.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )
        self.NotifyClient = channel.unary_unary(
                '/shopping.Market/NotifyClient',
                request_serializer=shopping__pb2.NotificationRequest.SerializeToString,
                response_deserializer=shopping__pb2.Response.FromString,
                )


class MarketServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisplaySellerItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToWishList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifyClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSeller,
                    request_deserializer=shopping__pb2.SellerInfo.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'SellItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SellItem,
                    request_deserializer=shopping__pb2.ItemInfo.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=shopping__pb2.ItemInfo.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=shopping__pb2.ItemID.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'DisplaySellerItems': grpc.unary_unary_rpc_method_handler(
                    servicer.DisplaySellerItems,
                    request_deserializer=shopping__pb2.SellerInfo.FromString,
                    response_serializer=shopping__pb2.ItemList.SerializeToString,
            ),
            'SearchItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchItem,
                    request_deserializer=shopping__pb2.SearchRequest.FromString,
                    response_serializer=shopping__pb2.ItemList.SerializeToString,
            ),
            'BuyItem': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyItem,
                    request_deserializer=shopping__pb2.BuyRequest.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'AddToWishList': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToWishList,
                    request_deserializer=shopping__pb2.WishListRequest.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'RateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RateItem,
                    request_deserializer=shopping__pb2.RatingRequest.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
            'NotifyClient': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyClient,
                    request_deserializer=shopping__pb2.NotificationRequest.FromString,
                    response_serializer=shopping__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'shopping.Market', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Market(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/RegisterSeller',
            shopping__pb2.SellerInfo.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/SellItem',
            shopping__pb2.ItemInfo.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/UpdateItem',
            shopping__pb2.ItemInfo.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/DeleteItem',
            shopping__pb2.ItemID.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisplaySellerItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/DisplaySellerItems',
            shopping__pb2.SellerInfo.SerializeToString,
            shopping__pb2.ItemList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/SearchItem',
            shopping__pb2.SearchRequest.SerializeToString,
            shopping__pb2.ItemList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuyItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/BuyItem',
            shopping__pb2.BuyRequest.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToWishList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/AddToWishList',
            shopping__pb2.WishListRequest.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/RateItem',
            shopping__pb2.RatingRequest.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifyClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shopping.Market/NotifyClient',
            shopping__pb2.NotificationRequest.SerializeToString,
            shopping__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
