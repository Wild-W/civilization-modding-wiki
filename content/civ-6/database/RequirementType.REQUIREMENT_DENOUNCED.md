---
tags:
- RequirementType
title: REQUIREMENT_DENOUNCED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DENOUNCED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_DENOUNCED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_DENOUNCED",
		"REQUIREMENT_DENOUNCED",
		1
	);

```
