---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_VERSUS_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_VERSUS_TYPE_MATCHES
>
> * Class: `COMBATS`
> * Arguments:
>	* CombatVersusType `String`

## Samples

```SQL {title="REQUIRES_COMBAT_IS_CITY_STRIKE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_COMBAT_IS_CITY_STRIKE",
		"REQUIREMENT_COMBAT_VERSUS_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_COMBAT_IS_CITY_STRIKE",
		"CombatVersusType",
		"COMBAT_DISTRICT_VS_UNIT"
	);
	```
