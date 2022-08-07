---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_SHORT_LIFE_GLORY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_SHORT_LIFE_GLORY
>
> * Class: `PLAYERS`
> * Parameters:
>	* EachWarDeclaredBonus `Integer`
>	* MajorWarBonus `Integer`
>	* MaxWarDeclaredBonus `Integer`
>	* NotAtWarPenalty `Integer`
>	* SinceWarPenaltyTurns `Integer`
>	* StatementKey `String`

## Samples
```SQL {title="AGENDA_SHORT_LIFE_GLORY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_SHORT_LIFE_GLORY",
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
		"AGENDA_SHORT_LIFE_GLORY",
		"EachWarDeclaredBonus",
		1
	),
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"MajorWarBonus",
		5
	),
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"MaxWarDeclaredBonus",
		5
	),
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"NotAtWarPenalty",
		"-6"
	),
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"SinceWarPenaltyTurns",
		40
	),
	(
		"AGENDA_SHORT_LIFE_GLORY",
		"StatementKey",
		"AGENDA_SHORT_LIFE_GLORY"
	);
	
```

