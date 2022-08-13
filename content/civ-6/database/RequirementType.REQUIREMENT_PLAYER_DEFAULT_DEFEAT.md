---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_DEFAULT_DEFEAT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_DEFAULT_DEFEAT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="DEFAULT_DEFEAT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"DEFAULT_DEFEAT_REQUIREMENT",
		"REQUIREMENT_PLAYER_DEFAULT_DEFEAT"
	);

```
