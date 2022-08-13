---
tags:
- RequirementType
title: REQUIREMENT_UNIT_HAS_ABILITY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_HAS_ABILITY
>
> * Class: `UNITS`
> * Arguments:
>	* UnitAbilityType `String`

## Samples

```SQL {title="AOE_REQUIRES_NO_SINGLE_COMBAT_STRENGTH_ABILITY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"AOE_REQUIRES_NO_SINGLE_COMBAT_STRENGTH_ABILITY",
		"REQUIREMENT_UNIT_HAS_ABILITY",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"AOE_REQUIRES_NO_SINGLE_COMBAT_STRENGTH_ABILITY",
		"UnitAbilityType",
		"ABILITY_GREAT_GENERAL_SINGLE_STRENGTH"
	);
	```
