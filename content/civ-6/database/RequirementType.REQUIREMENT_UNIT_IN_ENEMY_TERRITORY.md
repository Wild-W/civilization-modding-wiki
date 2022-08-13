---
tags:
- RequirementType
title: REQUIREMENT_UNIT_IN_ENEMY_TERRITORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_IN_ENEMY_TERRITORY
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="UNIT_IN_ENEMY_TERRITORY_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_IN_ENEMY_TERRITORY_REQUIREMENT",
		"REQUIREMENT_UNIT_IN_ENEMY_TERRITORY"
	);

```
