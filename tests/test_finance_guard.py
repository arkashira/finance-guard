import json
from finance_guard import FinanceGuard, RegulatoryRequirement, ComplianceCheck

def test_meet_regulatory_requirements():
    finance_guard = FinanceGuard()
    requirements = [RegulatoryRequirement.PCI_DSS, RegulatoryRequirement.GDPR]
    assert finance_guard.meet_regulatory_requirements(requirements)

def test_meet_regulatory_requirements_failure():
    finance_guard = FinanceGuard()
    requirements = [RegulatoryRequirement.PCI_DSS, RegulatoryRequirement.GDPR]
    finance_guard.compliance_checks.append(ComplianceCheck(RegulatoryRequirement.PCI_DSS, False))
    assert not finance_guard.meet_regulatory_requirements(requirements)

def test_provide_cryptographic_integrity():
    finance_guard = FinanceGuard()
    data = "test_data"
    result = finance_guard.provide_cryptographic_integrity(data)
    assert json.loads(result) == {"data": data}

def test_handle_audit():
    finance_guard = FinanceGuard()
    audit_data = "test_audit_data"
    result = finance_guard.handle_audit(audit_data)
    assert json.loads(result) == {"audit_data": audit_data}
