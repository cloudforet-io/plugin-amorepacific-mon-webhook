import logging
import unittest
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint
_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):

    def test_parse(self):

        options = {}

        raw_data_2 = {
                "event_time": "2021-06-27 02:16:43",
                "urgency": "0",
                "threshold": "뷰티체험단(Android)",
                "metric_value": "화면 로딩시간 (평균) [경고 >= 13 sec (10회 연속), 주의 >= 5 sec (3회 연속), 해제 < 5 sec] ",
                "status": "UP ",
                "summary": "08. IMQA>APMALL_AOS>뷰티체험단(Android)",
                "severity": "해제",
                "conditionlog": "화면 로딩시간 (평균) [0 ms (< 5 sec)]",
                "event_id": "32326932",
                "metric_name": "IMQA 응답시간 "
            }
        raw_data_3 = {
                "severity": "해제",
                "metric_name": "IMQA 응답시간 ",
                "summary": "08. IMQA>APMALL_AOS>회원(Android)",
                "event_time": "2021-06-27 02:16:44",
                "urgency": "0",
                "status": "UP ",
                "metric_value": "화면 로딩시간 (평균) [경고 >= 13 sec (10회 연속), 주의 >= 5 sec (3회 연속), 해제 < 5 sec] ",
                "event_id": "32326934",
                "conditionlog": "화면 로딩시간 (평균) [4.3 sec (< 5 sec)]",
                "threshold": "회원(Android)"
            }
        raw_data_4 = {
                "host_ip": "apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com",
                "metric_name": "롤백 발생 ",
                "conditionlog": "Rollback 수 [0 Count/s (= 0 Count/s)]",
                "status": "UP ",
                "event_id": "32326937",
                "summary": "07. DB그룹>10.INNISFREE GLOBAL>PostgreSQL 10 (apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com : INSFRPRDDB)>Databases>INSFRPRDDB",
                "severity": "해제",
                "metric_value": "Rollback 수 [주의 > 0 Count/s, 해제 = 0 Count/s] ",
                "threshold": "INSFRPRDDB",
                "event_time": "2021-06-27 02:16:50",
                "urgency": "0"
            }
        raw_data_5 = {
                "metric_value": "이벤트 탐지 [심각도: ERROR , 개행 포함, 내용 패턴: (?=.*member.*)(^((?!MLEC_MEMBER_NOT_FOUND).)*$)] ",
                "status": "UP ",
                "event_time": "2021-06-27 02:17:04",
                "urgency": "2",
                "conditionlog": "[1회 발생] 이벤트 탐지 [심각도: ERROR, 내용: [2021-06-27 02:17:01,299] [ERROR] [http-nio-8080-exec-10] [B2CMON_LOG.logging:124] [MON|2021-06-27 02:17:01,299|ERROR|M01||MobileWeb|member||||MLEC_MEMBER_AUTH_FAILURE|/MON] Fail. API=post:/v1/M01/ap/members/joinOnLogin, resultMsg=Authentication Failure [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:318 < ApMemberAuthRestApi.joinOnLogin:415 < GeneratedMethodAccessor4530.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
                "threshold": "ecp-api.log_member",
                "host_ip": "172.28.102.143",
                "severity": "경고",
                "metric_name": "회원_경고로그 ",
                "event_id": "32326942",
                "resource_name": "EAPWAS-172.28.102.143",
                "summary": "01. APMALL>EAPWAS-172.28.102.143>monitor group>ecp-api.log_member"
            }
        raw_data_6 = {
                "metric_value": "이벤트 탐지 [심각도: ERROR , 개행 포함, 내용 패턴: (?=.*member.*)(^((?!MLEC_MEMBER_NOT_FOUND).)*$)] ",
                "summary": "01. APMALL>EAPWAS-172.28.103.146>monitor group>ecp-api.log_member",
                "threshold": "ecp-api.log_member",
                "event_time": "2021-06-27 02:17:10",
                "status": "UP ",
                "conditionlog": "[1회 발생] 이벤트 탐지 [심각도: ERROR, 내용: [2021-06-27 02:17:08,176] [ERROR] [ http-nio-8080-exec-5] [B2CMON_LOG.logging:124] [MON|2021-06-27 02:17:08,176|ERROR|M01||MobileWeb|member||||MLEC_MEMBER_AUTH_FAILURE|/MON] Fail. API=post:/v1/M01/ap/members/joinOnLogin, resultMsg=Authentication Failure [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:318 < ApMemberAuthRestApi.joinOnLogin:415 < GeneratedMethodAccessor4391.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
                "host_ip": "172.28.103.146",
                "metric_name": "회원_경고로그 ",
                "severity": "경고",
                "resource_name": "EAPWAS-172.28.103.146",
                "urgency": "2",
                "event_id": "32326947"
            }
        raw_data_7 = {
                "threshold": "INSFRPRDDB",
                "conditionlog": "Rollback 수 [0.05 Count/s (> 0 Count/s)]",
                "status": "UP ",
                "urgency": "1",
                "summary": "07. DB그룹>10.INNISFREE GLOBAL>PostgreSQL 10 (apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com : INSFRPRDDB)>Databases>INSFRPRDDB",
                "event_time": "2021-06-27 02:17:50",
                "host_ip": "apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com",
                "severity": "주의",
                "metric_name": "롤백 발생 ",
                "metric_value": "Rollback 수 [주의 > 0 Count/s, 해제 = 0 Count/s] ",
                "event_id": "32326963"
            }
        raw_data_8 = {
                "event_id": "32326965",
                "conditionlog": "화면 로딩시간 (평균) [2.2 sec (< 5 sec)]",
                "metric_name": "IMQA 응답시간 ",
                "metric_value": "화면 로딩시간 (평균) [경고 >= 13 sec (10회 연속), 주의 >= 5 sec (3회 연속), 해제 < 5 sec] ",
                "status": "UP ",
                "urgency": "0",
                "summary": "08. IMQA>APMALL_iOS>장바구니(iOS)",
                "severity": "해제",
                "threshold": "장바구니(iOS)",
                "event_time": "2021-06-27 02:18:20"
            }
        raw_data_9 = {
                "status": "UP ",
                "metric_value": "Rollback 수 [주의 > 0 Count/s, 해제 = 0 Count/s] ",
                "conditionlog": "Rollback 수 [0 Count/s (= 0 Count/s)]",
                "summary": "07. DB그룹>10.INNISFREE GLOBAL>PostgreSQL 10 (apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com : INSFRPRDDB)>Databases>INSFRPRDDB",
                "urgency": "0",
                "host_ip": "apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com",
                "event_id": "32326981",
                "event_time": "2021-06-27 02:18:50",
                "severity": "해제",
                "threshold": "INSFRPRDDB",
                "metric_name": "롤백 발생 "
            }
        raw_data_10 = {
                "event_time": "2021-06-27 02:20:50",
                "host_ip": "apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com",
                "summary": "07. DB그룹>10.INNISFREE GLOBAL>PostgreSQL 10 (apne1-insfrprd-ecp-ecprds.cfqdcjczxddr.ap-northeast-1.rds.amazonaws.com : INSFRPRDDB)>Databases>INSFRPRDDB",
                "event_id": "32326983",
                "status": "UP ",
                "urgency": "1",
                "metric_value": "Rollback 수 [주의 > 0 Count/s, 해제 = 0 Count/s] ",
                "severity": "주의",
                "threshold": "INSFRPRDDB",
                "conditionlog": "Rollback 수 [0.02 Count/s (> 0 Count/s)]",
                "metric_name": "롤백 발생 "
            }
        raw_data_11 = {
            "status": "UP ",
            "summary": "01. APMALL>EAPWAS-172.28.103.124>monitor group>ecp-api.log_member",
            "urgency": "1",
            "resource_name": "EAPWAS-172.28.103.124",
            "metric_value": "이벤트 탐지 [심각도: WARN , 개행 포함, 내용 패턴: .*member.*] ",
            "metric_name": "회원_주의로그 ",
            "event_id": "32545700",
            "severity": "주의",
            "host_ip": "172.28.103.124",
            "threshold": "ecp-api.log_member",
            "conditionlog": "[1회 발생] 이벤트 탐지 [심각도: WARN, 내용: [2021-06-29 21:51:09,423] [ WARN] [http-nio-8080-exec-42] [B2CMON_LOG.logging:130] [MON|2021-06-29 21:51:09,423|WARN|M01||MobileApp|member||||MLEC_MEMBER_PASSWORD_NOT_MATCH|/MON] Fail. API=post:/v1/M01/ap/members/login, resultMsg=Password Not Match [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:284 < ApMemberAuthRestApi.memberLogin:334 < GeneratedMethodAccessor3346.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
            "event_time": "2021-06-29 09:51:12"
        }

        raw_data_both = {
            "status": "UP ",
            "event_time": "2021-06-29 09:50:51",
            "host_ip": "172.28.102.143",
            "metric_name": "회원_주의로그 ",
            "event_id": "32545698",
            "summary": "01. APMALL>EAPWAS-172.28.102.143>monitor group>ecp-api.log_member",
            "urgency": "1",
            #"conditionlog": "[1회 발생] 이벤트 탐지 [심각도: WARN, 내용: [2021-06-29 21:50:46,433] [ WARN] [http-nio-8080-exec-37] [B2CMON_LOG.logging:130] [MON|2021-06-29 21:50:46,433|WARN|M01||MobileWeb|member||||MLEC_MEMBER_AUTH_FAILURE|/MON] Fail. API=post:/v1/M01/ap/members/autoLogin, resultMsg=유효하지 않은 자격증명이 제시 [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:273 < ApMemberAuthRestApi.memberAutoLogin:373 < GeneratedMethodAccessor3491.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
            "resource_name": "EAPWAS-172.28.102.143",
            "threshold": "ecp-api.log_member",
            "metric_value": "이벤트 탐지 [심각도: WARN , 개행 포함, 내용 패턴: .*member.*] ",
            "severity": "주의"
        }

        raw_data_host_ip = {
            "host_ip": "172.28.102.143",
            "metric_name": "회원_주의로그 ",
            "event_id": "32545698",
            "summary": "01. APMALL>EAPWAS-172.28.102.143>monitor group>ecp-api.log_member",
            "urgency": "1",
            "event_time": "2021-06-29 09:50:51",
            "conditionlog": "[1회 발생] 이벤트 탐지 [심각도: WARN, 내용: [2021-06-29 21:50:46,433] [ WARN] [http-nio-8080-exec-37] [B2CMON_LOG.logging:130] [MON|2021-06-29 21:50:46,433|WARN|M01||MobileWeb|member||||MLEC_MEMBER_AUTH_FAILURE|/MON] Fail. API=post:/v1/M01/ap/members/autoLogin, resultMsg=유효하지 않은 자격증명이 제시 [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:273 < ApMemberAuthRestApi.memberAutoLogin:373 < GeneratedMethodAccessor3491.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
            "threshold": "ecp-api.log_member",
            "metric_value": "이벤트 탐지 [심각도: WARN , 개행 포함, 내용 패턴: .*member.*] ",
            "status": "UP ",
            "severity": "주의"
        }

        raw_data_resource_name = {
            "metric_name": "회원_주의로그 ",
            "event_id": "32545698",
            "summary": "01. APMALL>EAPWAS-172.28.102.143>monitor group>ecp-api.log_member",
            "urgency": "1",
            "event_time": "2021-06-29 09:50:51",
            "conditionlog": "[1회 발생] 이벤트 탐지 [심각도: WARN, 내용: [2021-06-29 21:50:46,433] [ WARN] [http-nio-8080-exec-37] [B2CMON_LOG.logging:130] [MON|2021-06-29 21:50:46,433|WARN|M01||MobileWeb|member||||MLEC_MEMBER_AUTH_FAILURE|/MON] Fail. API=post:/v1/M01/ap/members/autoLogin, resultMsg=유효하지 않은 자격증명이 제시 [MemberUtils.memberMonLoggingError:457 < ApMemberAuthRestApi.login:273 < ApMemberAuthRestApi.memberAutoLogin:373 < GeneratedMethodAccessor3491.invoke:-1 < DelegatingMethodAccessorImpl.invoke:43]]",
            "resource_name": "EAPWAS-172.28.102.143",
            "threshold": "ecp-api.log_member",
            "metric_value": "이벤트 탐지 [심각도: WARN , 개행 포함, 내용 패턴: .*member.*] ",
            "status": "UP ",
            "severity": "주의"
        }
        param_list = [
                      # raw_data_2,
                      # raw_data_3,
                      # raw_data_4,
                      # raw_data_5,
                      # raw_data_6,
                      # raw_data_7,
                      # raw_data_8,
                      # raw_data_9,
                        # raw_data_11,
                        raw_data_both,
                        raw_data_host_ip,
                        raw_data_resource_name
                      ]

        for idx, raw_dt in enumerate(param_list):
            print(f'#### {idx} #### ')
            parsed_data = self.monitoring.Event.parse({'options': options, 'data': raw_dt})
            print_json(parsed_data)
            print()


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)