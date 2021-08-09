#!/usr/bin/env python3
# 05/04/2021
# Dev: Cody Yarger
# Assignment 03 - Relational Database Management System (RDBMS)
''' Test unit for social netowrk '''

# pylint: disable=C0103
from unittest import TestCase
from pymongo import MongoClient
from users import UserCollection
#import pysnooper
#from loguru import logger
#from user_status import UserStatusCollection


class MongoDBConnectionTest():
    """ MongoDB Connection """

    def __init__(self, host='127.0.0.1', port=27017):
        """ note: be sure to use the ip address """
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


class UserDatabaseTest(TestCase):
    '''
        Tests for UserCollection methods
    '''
###############################################################################
# setUp and tearDown
###############################################################################

    # @pysnooper.snoop()
    def setUp(self):
        ''' Setup test database '''

        self.mongo = MongoDBConnectionTest()

        with self.mongo:

            # Database connection
            self.database = self.mongo.connection.media

            # Collection definition
            self.UserAccounts = self.database['UserAccounts']
            # self.user_test.drop()

            # self.user_test.delete_many({})

            # user_test collection documents
            users = [{'_id': 'id1',
                      'email': 'email1',
                      'user_name': 'name1',
                      'user_last_name': 'last1'},
                     {'_id': 'id2',
                      'email': 'email2',
                      'user_name': 'name2',
                      'user_last_name': 'last2'}]

            # insert documents in collection
            self.UserAccounts.insert_many(users)

            # instantiate UserCollection
            self.user_coll = UserCollection(self.database)

    # @pysnooper.snoop()
    def tearDown(self):
        ''' Teardown test database '''
        # self.user_test.delete_many({})
        self.UserAccounts.drop()
        self.user_coll = None
        #self.status_coll = None

###############################################################################
# users.py tests
###############################################################################

    def test_add_user(self):
        ''' Test add user '''
        expected = self.user_coll.add_user('id3', 'email3', 'name3', 'last3')
        self.assertTrue(expected)

    def test_add_user_false(self):
        ''' Test add user false'''
        expected = self.user_coll.add_user('id1', 'email4', 'name4', 'last4')
        self.assertFalse(expected)

    def test_modify_user(self):
        '''Test modify user'''
        expected = self.user_coll.modify_user('id1', 'emailx', 'namex', 'lastx')
        self.assertTrue(expected)

    def test_modify_user_false(self):
        ''' Test modify user false'''
        expected = self.user_coll.modify_user('idx', 'emailx', 'namex', 'lastx')
        self.assertFalse(expected)

    def test_delete_user(self):
        '''Test delete user'''
        expected = self.user_coll.delete_user('id1')
        self.assertTrue(expected)

    def test_delete_user_false(self):
        ''' Test delete user false'''
        expected = self.user_coll.delete_user('idx')
        self.assertFalse(expected)

    def test_search_user(self):
        '''Test search user'''
        expected = self.user_coll.search_user('id1')
        self.assertTrue(expected)

    def test_search_user_false(self):
        ''' Test search user false'''
        expected = self.user_coll.search_user('idx')
        self.assertFalse(expected)


# ###############################################################################
# # users_status.py tests
# ###############################################################################
#
#
#     def test_add_status(self):
#         '''Test add status'''
#         expected = self.status_coll.add_status('id1', 'statusx', 'text1')
#         self.assertTrue(expected)
#
#     def test_add_status_false(self):
#         ''' Test add status false'''
#         expected = self.status_coll.add_status('idx', 'status1', 'text1')
#         self.assertFalse(expected)
#
#     def test_modify_status(self):
#         '''Test modify status'''
#         expected = self.status_coll.modify_status('status1', 'id1', 'text')
#         self.assertTrue(expected)
#
#     def test_modify_status_false(self):
#         ''' Test modify status false'''
#         expected = self.status_coll.modify_status('statusx', 'id1', 'text1')
#         self.assertFalse(expected)
#
#     def test_delete_status(self):
#         '''Test delete status'''
#         expected = self.status_coll.delete_status('status1')
#         self.assertTrue(expected)
#
#     def test_delete_status_false(self):
#         ''' Test delete status false'''
#         expected = self.status_coll.delete_status('statusx')
#         self.assertFalse(expected)
#
#     def test_search_status(self):
#         '''Test search status'''
#         expected = self.status_coll.search_status('status1')
#         self.assertTrue(expected)
#
#     def test_search_status_false(self):
#         ''' Test search status false'''
#         expected = self.status_coll.search_status('statusx')
#         self.assertFalse(expected)
