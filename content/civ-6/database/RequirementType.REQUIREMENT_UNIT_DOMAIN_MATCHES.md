---
tags:
- RequirementType
title: REQUIREMENT_UNIT_DOMAIN_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_DOMAIN_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* UnitDomain `String`
>		* DOMAIN_LAND>		  DOMAIN_SEA

## Samples

```SQL {title="AOE_REQUIRES_LAND_DOMAIN"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"AOE_REQUIRES_LAND_DOMAIN",
		"REQUIREMENT_UNIT_DOMAIN_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"AOE_REQUIRES_LAND_DOMAIN",
		"UnitDomain",
		"DOMAIN_LAND"
	);
	
```
