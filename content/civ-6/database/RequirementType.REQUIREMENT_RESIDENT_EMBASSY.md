---
tags:
- RequirementType
title: REQUIREMENT_RESIDENT_EMBASSY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_RESIDENT_EMBASSY
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_RESIDENT_EMBASSY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_RESIDENT_EMBASSY",
		"REQUIREMENT_RESIDENT_EMBASSY"
	);


```
