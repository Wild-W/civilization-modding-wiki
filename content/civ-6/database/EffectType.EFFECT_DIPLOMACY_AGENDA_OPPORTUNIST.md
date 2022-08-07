---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_OPPORTUNIST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_OPPORTUNIST
>
> * Class: `PLAYERS`
> * Parameters:
>	* EachSurpriseWarBonus `Integer`
>	* NeverSurpriseWarPenalty `Integer`
>	* RecentSurpriseWarBonus `Integer`
>	* StatementKey `String`
>	* SurpriseWarDegradeTurns `Integer`

## Samples
```SQL {title="AGENDA_BACKSTABBER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_BACKSTABBER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_OPPORTUNIST",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_BACKSTABBER",
		"EachSurpriseWarBonus",
		1
	),
	(
		"AGENDA_BACKSTABBER",
		"NeverSurpriseWarPenalty",
		"-6"
	),
	(
		"AGENDA_BACKSTABBER",
		"RecentSurpriseWarBonus",
		15
	),
	(
		"AGENDA_BACKSTABBER",
		"StatementKey",
		"AGENDA_BACKSTABBER"
	),
	(
		"AGENDA_BACKSTABBER",
		"SurpriseWarDegradeTurns",
		3
	);
	
```

