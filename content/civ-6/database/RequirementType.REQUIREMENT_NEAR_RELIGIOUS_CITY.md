---
tags:
- RequirementType
title: REQUIREMENT_NEAR_RELIGIOUS_CITY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_NEAR_RELIGIOUS_CITY
>
> * Class: `PLAYERS`
> * Arguments:
>	* FriendlyCity `Boolean`

## Samples

```SQL {title="REQUIRES_UNIT_NEAR_ENEMY_RELIGIOUS_CITY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_UNIT_NEAR_ENEMY_RELIGIOUS_CITY",
		"REQUIREMENT_NEAR_RELIGIOUS_CITY"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_UNIT_NEAR_ENEMY_RELIGIOUS_CITY",
		"FriendlyCity",
		0
	);
	
```
