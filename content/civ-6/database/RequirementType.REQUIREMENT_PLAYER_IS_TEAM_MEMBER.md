---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_TEAM_MEMBER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_TEAM_MEMBER
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_IS_TEAM_MEMBER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		ProgressWeight
	)
VALUES
	(
		"REQUIRES_IS_TEAM_MEMBER",
		"REQUIREMENT_PLAYER_IS_TEAM_MEMBER",
		0
	);

```
