---
tags:
- RequirementType
title: REQUIREMENT_UNIT_ERA_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_ERA_TYPE_MATCHES
>
> * Class: `UNITS`
> * Arguments:
>	* EraType `String`
>		* [Eras.EraType]

## Samples

```SQL {title="AOE_REQUIRES_ATOMIC_UNIT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"AOE_REQUIRES_ATOMIC_UNIT",
		"REQUIREMENT_UNIT_ERA_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"AOE_REQUIRES_ATOMIC_UNIT",
		"EraType",
		"ERA_ATOMIC"
	);
	```
