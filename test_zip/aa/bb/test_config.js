/**
 * @copyright 2017-2020 Information & Communications Research Laboratories,
 *                      Industrial Technology Research Institute
 * @file Conf file reader UT
 */

'use strict';

const assert = require('chai').assert;
const config = require('../model/config');

describe('config::', function() {
  describe('init()', function() {
    context('when the input config is ok', function() {
      it('should return true', function(done) {
        const RDB_IP = '1.1.1.1';
        const RDB_PORT = 1234;
        const oldRdbIp = config.rdb_host;
        const oldRdbPort = config.rdb_port;
        // const oldSomething = config.something;
        const orgConfigStr = JSON.stringify(config);
        assert.isOk(config.init(JSON.stringify({
          'rdb_host': RDB_IP,
          'rdb_port': RDB_PORT,
        })));
        assert.strictEqual(RDB_IP, config.rdb_host);
        assert.strictEqual(RDB_PORT, config.rdb_port);

        // rollback
        config.rdb_host = oldRdbIp;
        config.rdb_port = oldRdbPort;

        // All other confs should not be changed
        assert.strictEqual(orgConfigStr, JSON.stringify(config));
        done();
      });
    });

    context('when the input config is not valid json', function() {
      it('should return false', function(done) {
        assert.isNotOk(config.init('{ "host": }'));
        done();
      });
    });

    context('when the type of the input config is wrong', function() {
      it('should return false', function(done) {
        assert.isNotOk(config.init(JSON.stringify({
          'manager': 123,
        })));
        done();
      });
    });

    context('when the type of the input config is wrong', function() {
      it('should return false', function(done) {
        assert.isNotOk(config.init(JSON.stringify({
          'host': null,
        })));
        done();
      });
    });
  });
});
