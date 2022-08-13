---
tags:
- RequirementType
title: REQUIREMENT_OPPONENT_UNIT_DOMAIN_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPPONENT_UNIT_DOMAIN_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* UnitDomain `String`
>		* DOMAIN_LAND>		  DOMAIN_SEA

## Samples

```SQL {title="OPPONENT_IS_AIR_UNIT_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_IS_AIR_UNIT_REQUIREMENTS",
		"REQUIREMENT_OPPONENT_UNIT_DOMAIN_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"OPPONENT_IS_AIR_UNIT_REQUIREMENTS",
		"UnitDomain",
		"DOMAIN_AIR"
	);
	```
