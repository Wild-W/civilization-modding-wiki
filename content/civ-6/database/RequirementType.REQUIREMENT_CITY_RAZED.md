---
tags:
- RequirementType
title: REQUIREMENT_CITY_RAZED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_RAZED
>
> * Class: `CITIES`
> * Arguments:
>	* OnlyOwnersCity `Boolean`

## Samples

```SQL {title="REQUIRES_PLAYER_MY_CITY_RAZED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_MY_CITY_RAZED",
		"REQUIREMENT_CITY_RAZED",
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
		"REQUIRES_PLAYER_MY_CITY_RAZED",
		"OnlyOwnersCity",
		1
	);
	
```
