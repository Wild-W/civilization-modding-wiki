---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_MILITARY_STRENGTH_LEAD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_MILITARY_STRENGTH_LEAD
>
> * Class: `PLAYERS`
> * Arguments:
>	* StrengthRatio `Integer`
>	* MinimumDelta `Integer`
>	* DomainType `String`

## Samples

```SQL {title="REQUIRES_HAS_HIGH_AIRPOWER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_AIRPOWER",
		"REQUIREMENT_PLAYER_MILITARY_STRENGTH_LEAD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HAS_HIGH_AIRPOWER",
		"DomainType",
		"DOMAIN_AIR"
	),
	(
		"REQUIRES_HAS_HIGH_AIRPOWER",
		"MinimumDelta",
		5
	),
	(
		"REQUIRES_HAS_HIGH_AIRPOWER",
		"StrengthRatio",
		"1.2"
	);
	```
