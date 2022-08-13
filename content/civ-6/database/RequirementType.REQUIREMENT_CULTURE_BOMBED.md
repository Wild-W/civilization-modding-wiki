---
tags:
- RequirementType
title: REQUIREMENT_CULTURE_BOMBED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CULTURE_BOMBED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_CULTURE_BOMBED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_CULTURE_BOMBED",
		"REQUIREMENT_CULTURE_BOMBED",
		1
	);


```
