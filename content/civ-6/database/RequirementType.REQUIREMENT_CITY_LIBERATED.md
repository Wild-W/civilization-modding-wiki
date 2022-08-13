---
tags:
- RequirementType
title: REQUIREMENT_CITY_LIBERATED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_LIBERATED
>
> * Class: `CITIES`
> * Arguments:
>	* OnlyOwnersCity `Boolean`

## Samples

```SQL {title="REQUIRES_PLAYER_CITY_LIBERATED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_CITY_LIBERATED",
		"REQUIREMENT_CITY_LIBERATED",
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
		"REQUIRES_PLAYER_CITY_LIBERATED",
		"OnlyOwnersCity",
		0
	);
	
```
